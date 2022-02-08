
# to use: source run.sh
cd /home/cf/venv/.venv
source bin/activate

cd /home/cf/flog/blog/
python manage.py runserver 0.0.0.0:9000
