Project's name: manga_universe

To start project:
1)sudo su (+ your password)

2)docker-compose up --build(to building docker and run server)

3)In another terminal: docker-compose exec web python manage.py migrate --noinput

1.In terminal:

docker ps -a

You must get name: yr-manga_web_1 sh

Next: docker exec -it magazin_altynai_web_1 sh

And write this for creating superuser(admin):

python manage.py createsuperuser

1)go to your browser and write in the search bar: 127.0.0.1:8000

If you need django-admin: (127.0.0.1:8000/admin/)

