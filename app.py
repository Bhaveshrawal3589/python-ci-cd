
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask on Render!'

@app.route('/new')
def new_route():
    return 'This is a new route for auto-deployment test!'


