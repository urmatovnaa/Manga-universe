# Generated by Django 4.1 on 2022-09-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title_app', '0005_delete_ratingstatistic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='genres', to='title_app.genre', verbose_name='Жанры'),
        ),
    ]
