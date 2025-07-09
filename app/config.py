import os
from pathlib import Path

# Load environment variables from .env file
basedir = Path(__file__).resolve().parent.parent

class Config:
    GITHUB_SECRET = os.environ.get("GITHUB_SECRET", 'FAIL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'sqlite:///' + os.path.abspath('stonewallNexus.db'))

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

# Choose config based on environment
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

current_env = os.getenv("FLASK_ENV", "development")
AppConfig = config_by_name[current_env]
