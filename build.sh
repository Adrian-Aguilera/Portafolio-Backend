#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

python manage.py migrate

python manage.py migrate Portafolio_App
python manage.py makemigrations Portafolio_App

# Apply any outstanding database migrations


python manage.py createsuperuser_Custom