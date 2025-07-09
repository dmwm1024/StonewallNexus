from flask import render_template
from app.chapter_admin import chapter_admin
from app.models.chapter import Chapter

@chapter_admin.route("/chapter-admin/<int:chapter_id>/users")
def list_users(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    return render_template("/chapter_admin/users/index.html", chapter=chapter)