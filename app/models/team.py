from app.extensions import db
from app.models.mixins import AuditMixin

class Team(db.Model, AuditMixin):
    """
    Represents a team competing in a season of a program.
    """

    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    season_id = db.Column(db.Integer, db.ForeignKey('seasons.id'), nullable=False)
    season = db.relationship('Season', back_populates='teams')

    home_matches = db.relationship('Match', back_populates='home_team', foreign_keys='Match.home_team_id')
    away_matches = db.relationship('Match', back_populates='away_team', foreign_keys='Match.away_team_id')

    registrations = db.relationship('Registration', back_populates='team', cascade='all, delete-orphan')