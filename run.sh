
# to use: source run.sh
cd /home/cf/program
source my_pyenv/bin/activate

cd /home/cf/program/flog/blog/
python manage.py runserver 0.0.0.0:9000
