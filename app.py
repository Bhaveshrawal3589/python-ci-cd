from flask import Flask, render_template_string, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from dotenv import load_dotenv
import logging

# NEW imports for database support
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env file
load_dotenv()
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key")

# --- DATABASE CONFIGURATION ---
# Use DATABASE_URL from .env for PostgreSQL connection
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# Disable modification tracking to save resources
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)

# --- FLASK-LOGIN setup ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# --- DATABASE MODEL ---
# Example simple model to store messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(256), nullable=False)

# Dummy user setup (unchanged)
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "testuser"
        self.password = "password"

# One hardcoded user
users = {"testuser": User("1")}

@login_manager.user_loader
def load_user(user_id):
    return users.get("testuser") if user_id == "1" else None

# --- ROUTES ---

@app.route('/')
def home():
    logging.info("Home route accessed")
    return "Hello from Flask!"

@app.route('/secret')
def secret():
    logging.info("Secret route accessed")
    return f"Secret message: {os.getenv('SECRET_MESSAGE', 'No secret found')}"

@app.route('/dashboard')
@login_required
def dashboard():
    return f"Welcome {current_user.name}! This is your dashboard."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and password == user.password:
            login_user(user)
            return redirect(url_for('dashboard'))
        return "Invalid credentials", 401

    return render_template_string('''
    <h2>Login</h2>
    <form method="POST">
        <input name="username" placeholder="Username" required><br><br>
        <input name="password" type="password" placeholder="Password" required><br><br>
        <input type="submit" value="Login">
    </form>
    ''')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# --- NEW: Route to test database ---
@app.route('/add-message')
def add_message():
    msg = Message(content="This is a test message.")
    db.session.add(msg)
    db.session.commit()
    return f"Message with ID {msg.id} added!"

if __name__ == "__main__":
    app.run(debug=True)
    


