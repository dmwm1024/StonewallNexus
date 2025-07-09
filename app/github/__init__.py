from flask import Blueprint

# Blueprint for authentication-related routes
github_bp = Blueprint('github', __name__, template_folder='templates')

from app.github.routes import github_routes