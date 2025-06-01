import logging
from flask import Flask

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/')
def hello():
    logging.info("Root endpoint '/' was accessed")
    return 'Hello from Flask on Render!'

@app.route('/new')
def new_route():
    logging.info("New endpoint '/new' was accessed")
    return 'This is a new route for auto-deployment test!'



