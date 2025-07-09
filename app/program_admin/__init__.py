from flask import Blueprint

# Blueprint for all admin routes
program_admin = Blueprint('program_admin', __name__, template_folder='templates')

from .routes import dashboard, officials, seasons, settings, teams