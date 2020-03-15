echo "Running migrates e migrations ..."
python3 pigmanage/manage.py makemigrations
python3 pigmanage/manage.py migrate
echo "Creating superuser ..."
python pigmanage/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')"