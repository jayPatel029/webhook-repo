# from flask import Flask, request, jsonify
# from pymongo import MongoClient
# from datetime import datetime
# import os
# from config import MONGO_URI

# app = Flask(__name__)
# client = MongoClient(MONGO_URI)
# db = client.github_events
# events_collection = db.events


# # @app.route('/webhook', methods=['POST'])
# # def webhook():
# #     data = request.json
# #     print("Received Webhook:", data)
# #     return '', 200


# @app.route('/status', methods=['GET'])
# def status():
#     try:
#         # Try pinging MongoDB
#         client.admin.command('ping')
#         return jsonify({
#             'flask_status': 'running',
#             'mongodb_status': 'connected'
#         }), 200
#     except Exception as e:
#         return jsonify({
#             'flask_status': 'running',
#             'mongodb_status': 'error',
#             'error_message': str(e)
#         }), 500



# @app.route('/webhook', methods=['POST'])
# def webhook():
#     event_type = request.headers.get('X-GitHub-Event')
#     payload = request.json

#     if not event_type or not payload:
#         return jsonify({'error': 'Invalid webhook'}), 400

#     event_data = {}

#     if event_type == "push":
#         head_commit = payload.get('head_commit', {})
#         commits = payload.get('commits', [])

#         event_data['author'] = commits[0]['author']['name'] if commits else payload['pusher']['name']
#         event_data['timestamp'] = head_commit.get('timestamp')
#         event_data['action_type'] = "push"
#         event_data['from_branch'] = None
#         event_data['to_branch'] = payload['ref'].split('/')[-1]
#         event_data['request_id'] = head_commit.get('id')  # Commit SHA

#     # Handle pull request (includes merged case)
#     elif event_type == "pull_request":
#         pr_data = payload.get('pull_request', {})

#         event_data['author'] = pr_data.get('user', {}).get('login')
#         event_data['timestamp'] = pr_data.get('created_at')
#         event_data['from_branch'] = pr_data.get('head', {}).get('ref')
#         event_data['to_branch'] = pr_data.get('base', {}).get('ref')
#         event_data['request_id'] = pr_data.get('id')  # PR ID

#         # Check for merged case
#         if pr_data.get('merged'):
#             event_data['action_type'] = "merge"
#             event_data['timestamp'] = pr_data.get('merged_at')
#         else:
#             event_data['action_type'] = "pull_request"

#     else:
#         # Ignore unsupported events
#         return jsonify({'status': f'Ignored event type: {event_type}'}), 200

#     # 🔍 Print exactly what you're storing in MongoDB
#     print("Storing event:", event_data)

#     # Store in MongoDB
#     events_collection.insert_one(event_data)

#     return jsonify({'status': 'success'}), 200



# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
