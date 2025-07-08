"""
run.py

Purpose:
    Entry point for the StonewallNexus Flask application. Initializes the app
    and runs the development server.

Usage:
    $ python run.py

Author:
    Kade
"""

from app import create_app
from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()