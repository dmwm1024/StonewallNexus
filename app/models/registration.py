from app.extensions import db
from app.models.mixins import AuditMixin
from datetime import datetime, timezone

class Registration(db.Model, AuditMixin):
    """
    Represents a user's registration in a season.
    """

    __tablename__ = 'registrations'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='registrations')

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    team = db.relationship('Team', back_populates='registrations')

    registered_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())