from flask import Flask

app = Flask(__name__)  # <--- this line defines the `app` that gunicorn looks for

@app.route('/')
def hello():
    return 'Hello from Flask on Render!'




