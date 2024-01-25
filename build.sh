pip install --upgrade pip
pip install --force-reinstall -U setuptools
pip install django
pip install dj_database_url
pip install django-environ
pip install psycopg2
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate