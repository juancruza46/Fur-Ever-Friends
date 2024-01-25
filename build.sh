pip install --upgrade pip
pip install --force-reinstall -U setuptools
pip install django
pip install environ
pip install os
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate