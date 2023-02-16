# Manga-universe
## Manga

Manga (Japanese: 漫画) are comics or graphic novels
originating from Japan. Most manga conform to
a style developed in Japan in the late 19th century,
and the form has a long history in earlier 
Japanese art. The term manga is used in Japan to 
refer to both comics and cartooning. Outside of 
Japan, the word is typically used to refer to 
comics originally published in the country.

## _Web manga_
Platform for reading manga, 
where the system of likes,
favorites is implemented. There is work with 
Excel, Celery, Docker, unit tests.
### Docker
To start project:
```sh
1)sudo su (+ your password)

2)docker-compose up --build(to building docker and run server)

3)In another terminal: docker-compose exec web python manage.py migrate --noinput
```
1.In terminal:
```sh
docker ps -a

You must get name: yr-manga_web_1 sh

Next: docker exec -it yr-manga_web_1 sh

And write this for creating superuser(admin):

python manage.py createsuperuser

1)go to your browser and write in the search bar: 127.0.0.1:8000

If you need django-admin: (127.0.0.1:8000/admin/)
```
