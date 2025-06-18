# Superheroes & Powers API

This is a Flask-based API to track heroes and their superpowers.

## Features

- RESTful API (GET, POST, PATCH)
- Hero-Power relationships
- Input validations
- Returns JSON responses with proper status codes

## Setup Instructions

```bash
git clone https://github.com/your-username/flask-superheroes-api.git
cd flask-superheroes-api
python3 -m venv ven
source venv/bin/activate
flask db upgrade
python app/seed.py
python run.py
