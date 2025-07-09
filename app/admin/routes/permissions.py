from flask import render_template
from app.admin import admin

@admin.route("/admin/permissions")
def permissions():
    return render_template("/admin/permissions/index.html")