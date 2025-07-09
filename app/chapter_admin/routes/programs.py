from flask import render_template, redirect, url_for, request
from app.chapter_admin import chapter_admin
from app.extensions import db
from app.models import Program
from app.models.chapter import Chapter

@chapter_admin.route('/chapter-admin/programs/new/<int:chapter_id>', methods=['GET', 'POST'])
def create_program(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')

        program = Program(name=name, description=description, chapter_id=chapter.id)

        db.session.add(program)
        db.session.commit()
        return redirect(url_for('chapter_admin.dashboard', chapter_id=chapter.id))
    return render_template("chapter_admin/programs/create.html", action="Create", chapter=chapter)

@chapter_admin.route('/chapter-admin/<int:chapter_id>/programs/<int:program_id>/edit', methods=['GET', 'POST'])
def edit_program(chapter_id, program_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    program = Program.query.get_or_404(program_id)

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')

        db.session.commit()
        return redirect(url_for('chapter_admin.dashboard', chapter=chapter))
    return render_template('chapter-admin/programs/edit.html', action="Edit", chapter=chapter, program=program)

@chapter_admin.route('/chapter-admin/<int:chapter_id>/programs/<int:program_id>/delete', methods=['POST'])
def delete_program(chapter_id, program_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    program = Program.query.get_or_404(program_id)

    db.session.delete(program)
    db.session.commit()
    return redirect(url_for('chapter_admin.dashboard', chapter=chapter))