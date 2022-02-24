@ECHO OFF
python -m pip install Django
pip install mysqlclient
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
PAUSE