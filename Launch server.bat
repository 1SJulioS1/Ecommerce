@echo off
cd venv\Scripts
call activate
cd ..
cd ..
python manage.py runserver
