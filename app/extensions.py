"""
extensions.py

Purpose:
    Initializes and exports Flask extensions for use across the app. This includes:
    - SQLAlchemy (database) and Metadata
    - Flask-Migrate (database migrations)
    - Flask-Login (user session management)

Usage:
    from app.extensions import db

Author:
    Kade
"""

import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData

# Add naming convention for constraints
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
    "ix": "ix_%(table_name)s_%(column_0_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
}


# Login manager for handling user authentication
login_manager = LoginManager()

# SQLAlchemy ORM instance
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

# Alembic-powered migration engine
migrate = Migrate()
