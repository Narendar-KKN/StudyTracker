# StudyTracker

A personal study-planning and progress-tracking web application built with Python and Django.

## Features

- Register, log in and log out securely using Django authentication
- Private dashboard for each account
- Create, edit, complete and delete study tasks
- Set study goals with target dates
- View task totals, completed tasks and completion percentage
- Responsive interface for desktop and mobile
- SQLite by default; optional MySQL configuration included

## Requirements

- Python 3.10 or newer
- pip
- Optional: MySQL Server if you want to use MySQL instead of SQLite

## Run on Windows

Open PowerShell in the folder containing `manage.py` and run:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations tracker
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

If PowerShell blocks activation, run this once in that terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Then activate the virtual environment again.

## Optional MySQL setup

SQLite is enabled by default so the project runs immediately. To use MySQL:

1. Create a database, for example `studytracker_db`, in MySQL.
2. Install the dependencies from `requirements.txt` (PyMySQL is included).
3. In `config/settings.py`, set `DB_ENGINE` to `mysql` and configure the environment variables below before running migrations.

PowerShell example:
```powershell
$env:DB_ENGINE="mysql"
$env:DB_NAME="studytracker_db"
$env:DB_USER="root"
$env:DB_PASSWORD="your_mysql_password"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
python manage.py migrate
```

For a local learning project, do not upload database passwords to GitHub. Use environment variables.

## GitHub upload

1. Create a new empty repository on GitHub named `StudyTracker`.
2. Extract this ZIP file.
3. Open PowerShell in the extracted `StudyTracker_Django_Project` folder.
4. Run:

```powershell
git init
git add .
git commit -m "Build StudyTracker Django application"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/StudyTracker.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Project structure

```text
StudyTracker_Django_Project/
├── config/
├── tracker/
│   ├── migrations/
│   ├── templates/tracker/
│   ├── static/tracker/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

## Resume description

**StudyTracker – Personal Study Planning Web Application**
- Developed a Django-based study planner with user authentication and personalized dashboards.
- Implemented task and goal management with create, update, delete and completion tracking.
- Designed responsive pages using HTML, CSS and Django templates.
- Integrated Django ORM with SQLite and documented optional MySQL configuration.

Only list MySQL as an implemented database on your resume after you have configured it and tested the project with MySQL.
