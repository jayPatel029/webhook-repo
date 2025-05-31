# app/webhook/routes.py

from flask import Blueprint, request, jsonify
from app.extensions import events_collection

# define webhook blueprint 
webhook_bp = Blueprint('webhook', __name__)

# this route will handle github webhook post requests
@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event')
    payload = request.json

    if not event_type or not payload:
        return jsonify({'error': 'Invalid webhook'}), 400

    # print(f"received: {payload}") 
    event_data = {}

    # handle events based on action_type
    # push event
    if event_type == "push":
        head_commit = payload.get('head_commit', {})
        commits = payload.get('commits', [])

        event_data['author'] = commits[0]['author']['name'] if commits else payload['pusher']['name']
        event_data['timestamp'] = head_commit.get('timestamp')
        event_data['action_type'] = "push"
        event_data['from_branch'] = None
        event_data['to_branch'] = payload['ref'].split('/')[-1]
        event_data['request_id'] = head_commit.get('id')
   
    # pull _requests events (open/close)
    elif event_type == "pull_request":
        pr_data = payload.get('pull_request', {})
        pr_action = payload.get('action')  # e.g., opened, closed, edited

        event_data['author'] = pr_data.get('user', {}).get('login')
        event_data['timestamp'] = pr_data.get('updated_at') or pr_data.get('created_at')
        event_data['from_branch'] = pr_data.get('head', {}).get('ref')
        event_data['to_branch'] = pr_data.get('base', {}).get('ref')
        event_data['request_id'] = pr_data.get('id')

        # check if pull_request was merged
        if pr_data.get('merge'):
            event_data['action_type'] = "merge"
            event_data['timestamp'] = pr_data.get('merged_at')
        else:
            event_data['action_type'] = f"pull_request_{pr_action}"  # e.g., pull_request_opened
    
    # Ignore unsupported event types
    else:
        return jsonify({'status': f'Ignored event type: {event_type}'}), 200

    print("Storing event:", event_data)
    events_collection.insert_one(event_data)

    return jsonify({'status': 'success'}), 200

# route to fetch all stored events
@webhook_bp.route('/events', methods=['GET'])
def get_events():
    try:
        events_cursor = events_collection.find()

        events = []
        for event in events_cursor:
            event['_id'] = str(event['_id'])
            events.append(event)

        return jsonify(events), 200

    except Exception as e:
        return jsonify({"error": "Could not fetch events", "details": str(e)}), 500

# Route to check the status of the API and MongoDB
@webhook_bp.route('/status', methods=['GET'])
def status():
    try:
        db_stats = events_collection.count_documents({})
        return jsonify({"status": "ok", "events_count": db_stats}), 200
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500


# init route
@webhook_bp.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "webhook API is running!"}), 200
