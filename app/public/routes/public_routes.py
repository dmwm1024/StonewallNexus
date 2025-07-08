"""
public_routes.py

Purpose:
    Defines the public-facing routes of the Stonewall Nexus application, including:
    - Landing page
    - Chapter selector
    - Public chapter detail pages

Usage:
    All routes are accessible via the 'public' blueprint at root-level URLs.

Author:
    Kade Kade <your-email@example.com>
"""

from flask import render_template
from app.public import public_bp
from app.models.chapter import Chapter

@public_bp.route("/")
def index():
    """
    Render the homepage of the site.

    Returns:
        str: Rendered index.html template.
    """

    return render_template('/index.html')

@public_bp.route('/chapter-selector')
def chapter_selector():
    """
    Display a list of all chapters for the user to choose from.

    Returns:
        str: Rendered chapter selector template with all chapters.
    """

    chapters = Chapter.query.all()
    return render_template('public/chapter_selector.html', chapters=chapters)

@public_bp.route('/chapter/<int:site_id>')
def chapter_page(chapter_id):
    """
    Render the public-facing page for a single chapter.

    Args:
        chapter_id (int): ID of the chapter to display.

    Returns:
        str: Rendered chapter page with chapter-specific data.
    """

    chapter = Chapter.query.get_or_404(chapter_id)
    return render_template('public/chapter_page.html', chapter=chapter)