from app.extensions import db
from app.models.mixins import AuditMixin

class Chapter(db.Model, AuditMixin):
    __tablename__ = 'chapters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    status = db.Column(db.String(100), default='Inactive')

    programs = db.relationship('Program', back_populates='chapter', lazy='dynamic')
    admins = db.relationship('ChapterAdminAssignment', back_populates='chapter', cascade='all, delete-orphan')
