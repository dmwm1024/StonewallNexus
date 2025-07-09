from flask import render_template

from app.models import Program
from app.program_admin import program_admin

@program_admin.route("/program-admin/<int:program_id>/seasons")
def seasons(program_id):
    program = Program.query.get_or_404(program_id)

    return render_template("/program_admin/seasons/index.html", program=program)