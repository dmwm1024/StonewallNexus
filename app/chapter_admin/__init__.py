from flask import Blueprint

# Blueprint for all admin routes
chapter_admin = Blueprint('chapter_admin', __name__, template_folder='templates')

from .routes import dashboard, programs, settings, users