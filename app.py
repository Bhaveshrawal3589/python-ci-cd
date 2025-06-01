from flask import Flask

app = Flask(__name__)  # <== This line defines the `app` object

@app.route('/')
def home():
    return 'Hello from Render!'


