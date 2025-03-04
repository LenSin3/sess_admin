release: python manage.py migrate  # Run migrations before starting the web process
web: gunicorn sess_admin.wsgi --bind 0.0.0.0:$PORT --log-file -

