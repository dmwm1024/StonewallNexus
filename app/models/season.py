from app.extensions import db
from app.models.mixins import AuditMixin
from datetime import datetime, timezone

class Season(db.Model, AuditMixin):
    """
    Represents a single competitive season for a program.
    """

    __tablename__ = 'seasons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'), nullable=False)
    program = db.relationship('Program', back_populates='seasons')

    teams = db.relationship('Team', back_populates='season', cascade='all, delete-orphan')
    matches = db.relationship('Match', back_populates='season', cascade='all, delete-orphan')

    def has_started(self):
        return datetime.now(timezone.utc) >= self.start_date

    def has_ended(self):
        return self.end_date is not None and datetime.now(timezone.utc) > self.end_date