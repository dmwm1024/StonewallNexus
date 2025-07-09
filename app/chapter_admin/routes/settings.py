from flask import render_template
from app.chapter_admin import chapter_admin
from app.models.chapter import Chapter

@chapter_admin.route("/chapter-admin/<int:chapter_id>/settings")
def settings(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    return render_template("/chapter_admin/settings/index.html", chapter=chapter)