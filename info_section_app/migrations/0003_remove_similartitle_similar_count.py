# Generated by Django 4.1 on 2022-08-27 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_section_app', '0002_alter_similartitle_similar_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='similartitle',
            name='similar_count',
        ),
    ]
