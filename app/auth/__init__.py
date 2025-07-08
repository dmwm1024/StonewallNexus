"""
__init__.py

Purpose:
    Sets up the authentication blueprint for Stonewall Nexus.

Usage:
    Import and register the blueprint in your application factory:

Author:
    Kade
"""

from flask import Blueprint

# Blueprint for authentication-related routes
auth_bp = Blueprint('auth', __name__, template_folder='templates')

from app.auth.routes import auth_routes