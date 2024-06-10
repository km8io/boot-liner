from flask import Flask, send_from_directory, abort, request, jsonify
import os
import logging
from os import walk

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Define the directory you want to serve
DIRECTORY = "/app/api/files"

@app.route('/')
def index():
    return "Welcome to the file server!"

@app.route('/notify')
def notify():
    machine = request.args.get('machine')
    message = request.args.get('message')
    logger.info(f"Request from {request.remote_addr} for machine {machine} with message {message}")
    return jsonify({'ip': request.remote_addr, 'machine': machine}), 200

@app.route('/files/<path:filename>')
def serve_file(filename):
    try:
        # Safely join the directory and the requested filename
        file_path = os.path.join(DIRECTORY, filename)
        
        logger.debug(f"Request for file: {filename}, resolved path: {file_path}")

        #logger.debug(os.getcwd())
        #f = []
        #for (dirpath, dirnames, filenames) in walk(DIRECTORY):
        #  f.extend(filenames)
        #  break
        #logger.debug(f)

        # Check if the file exists in the directory
        if os.path.isfile(file_path):
            #logger.debug("File exists")
            return send_from_directory(DIRECTORY, filename)
        else:
            abort(404)
    except Exception as e:
        abort(500)

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=8888)
