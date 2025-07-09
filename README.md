# SWNexus

## 🏳️‍🌈 Overview

**Stonewall Nexus** is a full-featured web application built for managing Stonewall Sports leagues. It streamlines scheduling, venue management, officiating assignments, team registrations, and role-based permissions across multiple chapters, sports, and seasons. Built BY Stonewall members FOR Stonewall members, it's designed to simplify league operations and empower volunteers at every level—from national to chapter-specific management.

- Dev Demo: https://kade.pythonanywhere.com/
  - Contact Kade for a test account to be created!

**Key Features:**
- Clean permission based role structures
- Management of sports, seasons, teams, venues, officials, and schedules
- (Future) Automatic (customizable) schedule generation and venue allocation
- (Future) Tournament Support & Scheduling - Live brackets for season finals or one-day tournaments alike!
- Intuitive Admin dashboards for leadership needs
- Intuitive Public-facing pages for members viewing schedules and program info
- Chapter and site management with linked user roles
- Flask-Login based authentication and user registration
- (Future) Payment processing

## 🧰 Tech Stack

| Layer        | Technology                                  |
|--------------|---------------------------------------------|
| Backend      | Python, Flask                               |
| ORM/Database | SQLAlchemy, PostgreSQL                      |
| Migrations   | Flask-Migrate (Alembic)                     |
| Frontend     | HTML, Jinja2, Bootstrap                     |
| Auth         | Flask-Login                                 |
| Forms        | Flask-WTF                                   |
| Dev Tools    | pytest, Faker, Flask CLI                    |
| Deployment   | WSGI (Gunicorn/Flask) or platform of choice |

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stonewallsync.git
cd stonewallsync
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a .env file in the root with the following:
```bash
# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development

# Security 
# SECRET_KEY= Allow it to use the default.

# Database
DATABASE_URL=sqlite:///stonewallNexus.db

# Other Configs
# GITHUB_SECRET = When/If you need this, I'll provide it.
```

### 5. Initialize the Database
To start fresh, init and migrate your own or use the upgrade command to be in sync with the dev branch.
```bash
flask db init
flask db migrate -m "Initialization"
flask db upgrade
```

### 6. (Optional) Load Seed Data
This will create a super admin account.
```bash
python scripts/seed_data.py
```

### 7. Run the Development Server
It should run with --debug automatically when ran locally, but just incase.
```bash
flask run --debug
```
Visit http://localhost:5000 to view the app.


## 🧑‍💻 Contribution Guide
Contributions are welcome! Here's how to get started:

#### 1. Fork this repository

#### 2. Create a new feature branch:
```bash
git checkout -b feature/your-feature-name
```

#### 3. Make your changes, add tests where appropriate

#### 4. Run tests and linting tools

#### 5. Commit your changes:
```bash
git commit -m "Add your descriptive message"
```

#### 6. Push to your fork and submit a Pull Request 

## Contribution Tips 
- Follow PEP8 and naming conventions
- Organize templates and routes by module
- Use UTC-aware datetime fields and clean SQLAlchemy models
  - Include the AuditMixin in all models.
- Ask questions!
- Dev Demo: https://kade.pythonanywhere.com/

## 🧠 Maintainers & Contact
This project is maintained by volunteers of Stonewall Sports.
For questions or feature requests, please open an issue or contact the project maintainer.