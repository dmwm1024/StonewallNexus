import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db
from app.models.user import User
from dotenv import load_dotenv; load_dotenv()

def seed_data():
    app = create_app()
    with app.app_context():
        print(app.config['SQLALCHEMY_DATABASE_URI'])
        print(app.config['FLASK_ENV'])

        db.create_all()

        if not User.query.filter_by(email='admin@admin.com').first():
            admin = User(
                email="admin@admin.com",
                username="admin",
                pronouns="He/Him/His",
                is_super_admin=True
            )
            admin.set_password('admin')
            db.session.add(admin)
            db.session.commit()
            print("✅ Admin user created.")
        else:
            print("ℹ️ Admin user already exists.")


if __name__ == "__main__":
    seed_data()