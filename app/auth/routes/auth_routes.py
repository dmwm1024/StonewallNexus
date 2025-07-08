"""
auth_routes.py

Purpose:
    Provides authentication routes for user login and logout using Flask-Login.

Usage:
    These routes are registered under the `auth` blueprint with the URL prefix `/auth`.

    - GET /auth/login: Render the login form
    - POST /auth/login: Process login credentials
    - GET /auth/logout: Log the user out

Author:
    Kade
"""

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from werkzeug.security import check_password_hash
from app.auth import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Render the login form or handle login submission.

    On POST, checks the provided email and password against the database.
    If valid, logs the user in and redirects them to the admin dashboard.

    Returns:
        str: Rendered login template (GET), or a redirect (POST)
    """

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash('Invalid email or password.')
    return render_template('/auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """
    Log the current user out and redirect to the login page.

    Returns:
        Redirect to the login route.
    """

    logout_user()
    return redirect(url_for('auth.login'))
