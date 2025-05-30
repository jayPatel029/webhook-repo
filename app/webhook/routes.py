# app/webhook/routes.py

from flask import Blueprint, request, jsonify
from app.extensions import events_collection

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event')
    payload = request.json

    if not event_type or not payload:
        return jsonify({'error': 'Invalid webhook'}), 400

    event_data = {}

    if event_type == "push":
        head_commit = payload.get('head_commit', {})
        commits = payload.get('commits', [])

        event_data['author'] = commits[0]['author']['name'] if commits else payload['pusher']['name']
        event_data['timestamp'] = head_commit.get('timestamp')
        event_data['action_type'] = "push"
        event_data['from_branch'] = None
        event_data['to_branch'] = payload['ref'].split('/')[-1]
        event_data['request_id'] = head_commit.get('id')

    elif event_type == "pull_request":
        pr_data = payload.get('pull_request', {})

        event_data['author'] = pr_data.get('user', {}).get('login')
        event_data['timestamp'] = pr_data.get('created_at')
        event_data['from_branch'] = pr_data.get('head', {}).get('ref')
        event_data['to_branch'] = pr_data.get('base', {}).get('ref')
        event_data['request_id'] = pr_data.get('id')

        if pr_data.get('merged'):
            event_data['action_type'] = "merge"
            event_data['timestamp'] = pr_data.get('merged_at')
        else:
            event_data['action_type'] = "pull_request"

    else:
        return jsonify({'status': f'Ignored event type: {event_type}'}), 200

    print("Storing event:", event_data)
    events_collection.insert_one(event_data)

    return jsonify({'status': 'success'}), 200


@webhook_bp.route('/events', methods=['GET'])
def get_events():
    try:
        # Fetch events sorted by most recent timestamp
        events_cursor = events_collection.find().sort("timestamp", -1)
        
        # Convert MongoDB cursor to a list of dicts
        events = []
        for event in events_cursor:
            event['_id'] = str(event['_id'])  # Convert ObjectId to string
            events.append(event)
        
        return jsonify(events), 200
    except Exception as e:
        return jsonify({"error": "Could not fetch events", "details": str(e)}), 500



@webhook_bp.route('/status', methods=['GET'])
def status():
    try:
        # Just a dummy read to verify connection
        events_collection.find_one()
        return jsonify({'status': 'MongoDB connected'}), 200
    except Exception as e:
        return jsonify({'status': 'MongoDB error', 'error': str(e)}), 500
