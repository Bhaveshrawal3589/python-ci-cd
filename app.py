import logging
from flask import Flask, request

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Automatically log every route access
@app.before_request
def log_request_info():
    logging.info(f"Route accessed: {request.method} {request.path} | IP: {request.remote_addr}")

@app.route('/')
def hello():
    return 'Hello from Flask on Render!'

@app.route('/new')
def new_route():
    return 'This is a new route for auto-deployment test!'



