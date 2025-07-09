from flask import render_template
from app.chapter_admin import chapter_admin
from app.models.chapter import Chapter
from app.models.program import Program

@chapter_admin.route("/chapter-admin/<int:chapter_id>/dashboard")
def dashboard(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    programs = Program.query.filter_by(chapter_id=chapter.id).all()

    return render_template("/chapter_admin/dashboard.html", chapter=chapter, programs=programs)