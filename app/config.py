"""
config.py

Purpose:
    Loads Flask configuration using environment variables (from .env).

Usage:
    app.config.from_object(Config)

Author:
    Kade Kade <your-email@example.com>
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))

class Config:
    """
    Base configuration class used in development by default.
    Extend this class for specific environments.
    """
    GITHUB_SECRET = os.environ.get("GITHUB_SECRET", 'FAIL')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'sqlite:///' + os.path.abspath('stonewallNexus.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = FLASK_ENV == "development"
