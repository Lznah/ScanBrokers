from flask import Flask, request, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    """Landing page."""
    return render_template(
        'home.html',
        title="you love stalking, we love it to",
        description="Smarter page templates with Flask & Jinja."
    )


@app.route('/')
def index():
    return 'NI-PYT je nejlepší předmět na FITu!'

@app.route('/broker/search')
def search():
    query = request.args.get('query')
    return render_template('search')