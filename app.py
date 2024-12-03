from flask import Flask, request, jsonify
import datetime
import os
app = Flask(__name__)
# Define the base log directory
LOG_DIR = r"C:\Arcgis_API\user_activity_logs"
@app.route('/logAccess', methods=['POST'])
def log_access():
   data = request.get_json()
   username = data.get('username')
   app_name = data.get('appName')
   timestamp = datetime.datetime.now()
   # Create a log filename based on the current month
   log_filename = f"dashboard_logs_{timestamp.year}_{timestamp.strftime('%b')}.log"
   log_path = os.path.join(LOG_DIR, log_filename)
   log_entry = f"{timestamp.isoformat()} - User: {username}, App: {app_name}\n"
   # Append log entry to the monthly log file
   with open(log_path, 'a') as log_file:
       log_file.write(log_entry)
   return jsonify({'message': 'Log entry created'}), 200
if __name__ == '__main__':
   app.run(debug=True, port=5000)