"""
users.py

Purpose:
    Provides admin functionality for viewing, creating, and editing users,
    including assigning chapter and program roles.

Usage:
    Routes are part of the admin blueprint and typically accessible under `/admin/users`.

Author:
    Kade
"""

from flask import render_template, request, flash, redirect, url_for
from app.admin import admin
from app.models.user import User
from app.models.chapter import Chapter
from app.extensions import db
from flask_login import current_user
from werkzeug.security import check_password_hash

@admin.route('/admin/users')
def list_users():
    """
    Display a list of all users.

    Returns:
        Rendered HTML template with list of users.
    """

    users = User.query.all()
    chapters = Chapter.query.filter_by(status='Active').all()

    return render_template("/admin/users/index.html", users=users, chapters=chapters)

@admin.route('/admin/users/create', methods=['GET', 'POST'])
def create_user():
    """
    Handle the creation of a new user.

    Retrieves form data (`username`, `email`, `password`, `pronouns`),
    validates inputs, checks for duplicates, and saves the user to the database.

    Returns:
        Redirect to the user list with a flash message.
    """

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    pronouns = request.form.get('pronouns')

    if not all([username, email, password, pronouns]):
        flash("All fields are required.", "danger")
        return redirect(url_for('admin.list_users'))

    if User.query.filter_by(email=email).first():
        flash("A user with that email already exists.", "danger")
        return redirect(url_for('admin.list_users'))

    user = User(username=username, email=email, pronouns=pronouns)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    flash(f"User {username} created successfully.", "success")
    return redirect(url_for('admin.list_users'))

@admin.route('/admin/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    user_chapter_ids = [role.chapter_id for role in user.chapter_admin_roles]
    user_program_ids = [role.program_id for role in user.program_admin_roles]
    chapters=Chapter.query.filter_by(status="Active").all()


    if request.method == 'POST':
        was_super_admin = user.is_super_admin
        will_be_super_admin = request.form.get('is_super_admin') == 'true'

        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.pronouns = request.form.get('pronouns')
        new_password = request.form.get('password')
        if new_password:
            user.set_password(new_password)

        # Only validate password if changing super admin status
        if not will_be_super_admin == was_super_admin:
            admin_password = request.form.get('admin_password')
            if not admin_password or not current_user.check_password(admin_password):
                flash("Password confirmation failed. Super Admin access not granted.", "danger")
                return redirect(url_for('admin.edit_user', user_id=user.id))
            user.is_super_admin = will_be_super_admin

        db.session.commit()
        flash(f"User {user.username} updated successfully.", "success")
        return redirect(url_for('admin.list_users'))

    return render_template('/admin/users/edit.html', user=user, user_chapter_ids=user_chapter_ids, user_program_ids=user_program_ids, chapters=chapters)
