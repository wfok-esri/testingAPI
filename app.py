from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import os
app = Flask(__name__)
# Define the base log directory
LOG_DIR = r"E:\GOPMS\logs\useraccess"
# Ensure the log directory exists
if not os.path.exists(LOG_DIR):
   os.makedirs(LOG_DIR)
@app.route('/logAccess', methods=['POST'])
def log_access():
   data = request.get_json()
   username = data.get('username')
   app_name = data.get('appName')
   timestamp = datetime.datetime.now()
   # Create a log filename based on the current day
   log_filename = f"useraccess_{timestamp.strftime('%Y-%m-%d')}.log"
   log_path = os.path.join(LOG_DIR, log_filename)
   log_entry = f"{timestamp.isoformat()} - User: {username}, App: {app_name}\n"
   # Append log entry to the daily log file
   try:
       with open(log_path, 'a') as log_file:
           log_file.write(log_entry)
       return jsonify({'message': 'Log entry created'}), 200
   except Exception as e:
       return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
   app.run(debug=True, port=5000)
