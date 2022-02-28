@ECHO OFF
python manage.py loaddata fixtures.json
python manage.py runserver
PAUSE