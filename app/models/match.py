from app.extensions import db
from app.models.mixins import AuditMixin
from datetime import datetime, timezone

class Match(db.Model, AuditMixin):
    """
    Represents a scheduled match between two teams in a season.
    """

    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    match_date = db.Column(db.DateTime, nullable=False)

    season_id = db.Column(db.Integer, db.ForeignKey('seasons.id'), nullable=False)
    season = db.relationship('Season', back_populates='matches')

    home_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

    home_team = db.relationship('Team', back_populates='home_matches', foreign_keys=[home_team_id])
    away_team = db.relationship('Team', back_populates='away_matches', foreign_keys=[away_team_id])

    venue = db.Column(db.String(100), nullable=True)
    location_notes = db.Column(db.String(255), nullable=True)

    def is_upcoming(self):
        return self.match_date > datetime.now(timezone.utc)

    def is_past(self):
        return self.match_date < datetime.now(timezone.utc)