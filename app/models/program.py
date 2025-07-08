from app.extensions import db
from app.models.mixins import AuditMixin

class Program(db.Model, AuditMixin):
    """
    Represents a sports program within a chapter.
    """

    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'))
    chapter = db.relationship('Chapter', back_populates='programs')

    seasons = db.relationship('Season', back_populates='program', cascade='all, delete-orphan')
    admins = db.relationship('ProgramAdminAssignment', back_populates='program', cascade='all, delete-orphan')

