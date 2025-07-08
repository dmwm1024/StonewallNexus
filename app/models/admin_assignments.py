from app.extensions import db
from app.models.mixins import AuditMixin

class ChapterAdminAssignment(db.Model, AuditMixin):
    """
    Links a user to a chapter as an administrator.
    """

    __tablename__ = 'chapter_admin_assignments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)

    user = db.relationship('User', back_populates='chapter_admin_roles')
    chapter = db.relationship('Chapter', back_populates='admins')

class ProgramAdminAssignment(db.Model, AuditMixin):
    """
    Links a user to a program as an administrator.
    """

    __tablename__ = 'program_admin_assignments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'), nullable=False)

    user = db.relationship('User', back_populates='program_admin_roles')
    program = db.relationship('Program', back_populates='admins')