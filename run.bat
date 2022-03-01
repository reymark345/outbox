@ECHO OFF
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures.json
python manage.py runserver
PAUSE