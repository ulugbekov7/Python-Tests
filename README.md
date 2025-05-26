This Flask project requires proper environment setup and database configuration to run correctly.
Prerequisites

Python 3.7 or higher
PostgreSQL installed and running
pip (Python package installer)

Setup Instructions
1) Create and Activate Virtual Environment
bash# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
2) Install Dependencies
bashpip install -r requirements.txt

3) Database Setup
Create PostgreSQL Database

1. Create the database:

sqlCREATE DATABASE test_24;

Exit PostgreSQL:

sql\q
Initialize Database Tables

2. Open Flask shell:

bashflask shell

3. Create all database tables:

pythonfrom app import db
db.create_all()
exit()

4) Run the Application
bashflask run
The application will be available at http://127.0.0.1:5000
