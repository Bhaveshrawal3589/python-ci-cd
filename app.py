from flask import Flask
from dotenv import load_dotenv
import os
import logging

load_dotenv()  # Load variables from .env

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    logging.info("Home route accessed")
    return "Hello from Flask!"

@app.route('/secret')
def secret():
    secret_msg = os.getenv("SECRET_MESSAGE", "No secret found")
    return f"Secret message: {secret_msg}"

if __name__ == "__main__":
    app.run(debug=True)




