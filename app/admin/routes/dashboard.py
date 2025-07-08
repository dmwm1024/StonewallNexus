"""
dashboard.py

Purpose:
    Defines the main admin dashboard view, which provides an overview
    of chapter management features and shortcuts for administrators.

Usage:
    This module is included in the admin blueprint, accessible at /admin/dashboard.

Author:
    Kade
"""

from flask import render_template
from app.admin import admin
from app.models.user import User
from app.models.chapter import Chapter

@admin.route("/admin/dashboard")
def dashboard():
    """
    Display the admin dashboard page.

    Returns:
        Rendered HTML dashboard template.
    """

    users = User.query.all()
    chapters = Chapter.query.all()
    return render_template("/admin/dashboard.html", chapters=chapters, users=users)