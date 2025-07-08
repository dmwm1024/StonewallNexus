from .user import User
"""
__init__.py

Purpose:
    Used to initialize the models package.

Usage:
    Used to import key models.

Author:
    Kade
"""

from .chapter import Chapter
from .program import Program
from .team import Team
from .season import Season
from .match import Match
from .registration import Registration
from .admin_assignments import ChapterAdminAssignment, ProgramAdminAssignment
from app.models.mixins import AuditMixin

AuditMixin.register_audit_listeners(User)
AuditMixin.register_audit_listeners(Chapter)
AuditMixin.register_audit_listeners(Program)
AuditMixin.register_audit_listeners(Team)
AuditMixin.register_audit_listeners(Season)
AuditMixin.register_audit_listeners(Match)
AuditMixin.register_audit_listeners(Registration)
AuditMixin.register_audit_listeners(ChapterAdminAssignment)
AuditMixin.register_audit_listeners(ProgramAdminAssignment)

