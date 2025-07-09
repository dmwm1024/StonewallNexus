"""
__init__.py

Purpose:
    Initializes the admin blueprint for Stonewall Nexus. This blueprint is
    responsible for rendering and routing all admin-level views.

Usage:
    Import and register the blueprint in your application factory:
        from app.admin import admin_bp
        app.register_blueprint(admin_bp, url_prefix="/admin")

        This is done in app/__init__.py

Author:
    Kade
"""

from flask import Blueprint

# Blueprint for all admin routes
admin = Blueprint('admin', __name__, template_folder='templates')

from .routes import dashboard, users, chapters