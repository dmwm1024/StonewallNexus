"""
chapters.py

Purpose:
    Contains route handlers for creating, editing, viewing, and deleting
    chapters within the admin panel.

Usage:
    This module is registered as part of the admin blueprint.
    Endpoints typically follow /admin/chapters/*.

Author:
    Kade
"""

from flask import render_template, request, url_for, redirect, flash
from app.admin import admin
from app.models.chapter import Chapter
from app.extensions import db

@admin.route("/admin/chapters")
def list_chapters():
    """
    Display a list of all chapters.

    Returns:
        Rendered HTML template showing all chapters.
    """

    chapters = Chapter.query.all()
    return render_template("/admin/chapters/index.html", chapters=chapters)

@admin.route("/admin/chapters/new", methods=["GET", "POST"])
def create_chapter():
    """
    Render form to create a new chapter.

    Returns:
        GET: Rendered form template for creating a new chapter.
        POST: Redirect to chapter list if successful.
    """

    if request.method == "POST":
        name = request.form.get("name")
        city = request.form.get("city")
        state = request.form.get("state")
        status = request.form.get("status")

        chapter = Chapter(name=name, city=city, state=state, status=status)

        db.session.add(chapter)
        db.session.commit()
        flash(f"Chapter {name} created successfully.", "success")
        return redirect(url_for("admin.list_chapters"))

    return render_template("/admin/chapters/form.html", action="Create")

@admin.route("/admin/chapters/<int:chapter_id>/edit", methods=["GET", "POST"])
def edit_chapter(chapter_id):
    """
    Render form to edit an existing chapter and handle updates.

    Args:
        chapter_id (int): The ID of the chapter to edit.

    Returns:
        GET: Rendered edit form.
        POST: Redirect to chapter list if updated.
    """

    chapter = Chapter.query.get_or_404(chapter_id)
    if request.method == "POST":
        chapter.name = request.form.get("name")
        chapter.city = request.form.get("city")
        chapter.state = request.form.get("state")
        chapter.status = request.form.get("status")
        db.session.commit()
        return redirect(url_for("admin.list_chapters"))
    return render_template("/admin/chapters/form.html", action="Edit", chapter=chapter)

@admin.route("/admin/chapters/<int:chapter_id>/delete", methods=["POST"])
def delete_chapter(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    db.session.delete(chapter)
    db.session.commit()
    return redirect(url_for("admin.list_chapters"))