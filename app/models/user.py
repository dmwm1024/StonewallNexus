from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.mixins import AuditMixin

class User(db.Model, UserMixin, AuditMixin):
    """
    Represents a user in the system. Handles authentication, role assignment,
    and relationships to chapters and programs.

    Inherits:
        - UserMixin: Flask-Login integration
        - AuditMixin: Timestamps for created_at and updated_at
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pronouns = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_super_admin = db.Column(db.Boolean, nullable=False, default=False)

    registrations = db.relationship('Registration', back_populates='user', cascade='all, delete-orphan')
    chapter_admin_roles = db.relationship('ChapterAdminAssignment', back_populates='user', cascade='all, delete-orphan')
    program_admin_roles = db.relationship('ProgramAdminAssignment', back_populates='user', cascade='all, delete-orphan')

    def set_password(self, password):
        """
        Hash and store a user's password.

        Args:
            password (str): The raw password to hash.
        """

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verify a password against the stored hash.

        Args:
            password (str): The raw password to verify.

        Returns:
            bool: True if the password is correct, False otherwise.
        """

        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        """
        Check if the user is a super admin.

        Returns:
            bool: True if the user is a super admin.
        """

        return self.is_super_admin

    @property
    def is_chapter_admin(self, chapter=None):
        """
        Check if the user is a chapter admin for a specific chapter (or any).

        Args:
            chapter (Chapter, optional): A specific chapter to check against.

        Returns:
            bool: True if the user is a chapter admin for a specific chapter (or any if chapter is not provided).
        """

        if chapter is not None:
            return any(role.chapter_id == chapter.id for role in self.chapter_admin_roles)
        return len(self.chapter_admin_roles) > 0

    @property
    def is_program_admin(self, program=None):
        """
        Check if the user is a program admin for a specific program (or any).

        Args:
            program (Program, optional): A specific program to check against.

        Returns:
            bool: True if the user is a program admin.
        """

        if program is not None:
            return any(role.program_id == program.id for role in self.program_admin_roles)
        return len(self.program_admin_roles) > 0