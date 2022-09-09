# Generated by Django 4.1 on 2022-09-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title_app', '0003_alter_rating_star'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
    ]