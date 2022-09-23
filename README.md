PROJECT'S NAME: manga_universe

TO START PROJECT:
1)sudo su (+ your password)

2)docker-compose up --build(to building docker and run server)

3)In another terminal: docker-compose exec web python manage.py migrate --noinput

4)go to your browser and write in the search bar: 127.0.0.1:8000

IF YOU NEED TO GO IN DJANGO ADMIN PANEL: (127.0.0.1:8000/admin/)

1.In terminal:

docker ps -a

YOU MUST GET A NAME yr-manga_web_1 sh

NEXT: docker exec -it magazin_altynai_web_1 sh

AND WRITE THIS FOR CREATING SUPERUSER(ADMIN):

python manage.py createsuperuser

ANYTHING URLS YOU HAVE IN DIR "magazine", FILE "urls.py"

TESTS: DIR "account_app", FILE "tests.py"

1)go to your browser and write in the search bar: 127.0.0.1:8000

IF YOU NEED TO GO IN DJANGO ADMIN PANEL: (127.0.0.1:8000/admin/)


