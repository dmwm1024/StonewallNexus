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

@admin.route('/admin/users/create')
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
    """
    Display and handle form submission for editing an existing user.

    Args:
        user_id (int): ID of the user to edit.

    GET:
        Renders the edit form pre-filled with user info and assigned roles.

    POST:
        Updates user attributes (`username`, `email`, `pronouns`, `password`)
        and commits the changes.

    Returns:
        Rendered form or redirect with a flash message.
    """

    user = User.query.get_or_404(user_id)
    user_chapter_ids = [role.chapter_id for role in user.chapter_admin_roles]
    user_program_ids = [role.program_id for role in user.program_admin_roles]
    chapters=Chapter.query.filter_by(status="Active").all()


    if request.method == 'POST':
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.pronouns = request.form.get('pronouns')
        user.set_password(request.form.get('password'))

        db.session.commit()
        flash(f"User {user.username} updated successfully.", "success")
        return redirect(url_for('admin.list_users'))

    return render_template('/admin/users/edit.html', user=user, user_chapter_ids=user_chapter_ids, user_program_ids=user_program_ids, chapters=chapters)
