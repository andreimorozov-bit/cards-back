# create virtual environment

python -m venv env_name

# activate it

env_name/scripts/activate

# install packages

pip install -r requirements.txt

# make database migrations

python manage.py makemigrations
python manage.py migrate

# run server on http://localhost:8000/

python manage.py runserver

# endpoints

get cards/
post cards/
get cards/id/
patch cards/id/
del cards/id/

get products/
post products/
get products/id/
patch products/id/
del products/id/

get purchases/
post purchases/

post auth/register/
post auth/login/
post auth/login/refresh
