"""
__init__.py

Purpose:
    Initializes the public blueprint for serving all unauthenticated views
    such as the home page, chapter selector, and public chapter pages.

Usage:
    Import and register the blueprint in the application factory:
        from app.public import public_bp
        app.register_blueprint(public_bp)

Author:
    Kade
"""

from flask import Blueprint

# Import routes to associate them with the blueprint
public_bp = Blueprint('public', __name__, template_folder='templates')

from .routes import public_routes