# Generated by Django 4.1 on 2022-08-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_section_app', '0003_remove_similartitle_similar_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='similartitle',
            name='similar_count',
            field=models.IntegerField(default=0),
        ),
    ]
