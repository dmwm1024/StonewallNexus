"""
mixins.py

Purpose:
    Contains reusable SQLAlchemy model mixins, such as AuditMixin for tracking
    creation and update timestamps.

Usage:
    Inherit from AuditMixin in any model to automatically track timestamps.
        - Also register it's usage in models/__init__.py

Author:
    Kade
"""

from datetime import datetime, timezone
from flask_login import current_user
from app.extensions import db
from sqlalchemy import event

class AuditMixin(object):
    """
    Adds created_at and updated_at timestamp fields to a model.
    """
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)

    @staticmethod
    def _set_created_fields(mapper, connection, target):
        print(f"[AUDIT] Insert on {target}")
        if hasattr(current_user, 'id'):
            print(f"[AUDIT] current_user.id = {current_user.id}")
            if not target.created_by:
                target.created_by = current_user.id
            target.updated_by = current_user.id

    @staticmethod
    def _set_updated_fields(mapper, connection, target):
        if hasattr(current_user, "id"):
            target.updated_by = current_user.id

    # Register event listeners for all models using AuditMixin
    @classmethod
    def register_audit_listeners(cls, model_class):
        event.listen(model_class, 'before_insert', cls._set_created_fields)
        event.listen(model_class, 'before_update', cls._set_updated_fields)