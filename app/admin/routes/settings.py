from flask import render_template
from app.admin import admin

@admin.route("/admin/settings")
def settings():
    return render_template("/admin/settings/index.html")