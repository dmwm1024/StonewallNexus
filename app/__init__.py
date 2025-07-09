"""
__init__.py

Purpose:
    Initializes the Flask application using the application factory pattern.
    Registers extensions, blueprints, error handlers, and CLI commands.

Usage:
    Import `create_app()` and call it to instantiate the Flask app:
        from app import create_app
        app = create_app()

Author:
    Kade
"""

from flask import Flask
from app.models.user import User
from app.extensions import db, migrate, login_manager

def create_app():
    """
    Flask application factory.

    Args:
        config_class (Type): The configuration class to use.

    Returns:
        Flask: Configured Flask application instance.
    """

    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register GitHub webhook routes
    from app.github import github_bp
    app.register_blueprint(github_bp)

    # Register blueprints and routes
    from app.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.public import public_bp
    app.register_blueprint(public_bp)

    from app.admin import admin
    app.register_blueprint(admin)

    return app