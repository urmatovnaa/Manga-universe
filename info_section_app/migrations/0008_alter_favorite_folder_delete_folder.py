# Generated by Django 4.1 on 2022-09-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_section_app', '0007_relatedtitle_user_folder_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='folder',
            field=models.CharField(choices=[('1', 'Читаю'), ('2', 'Прочитано'), ('3', 'Брошено'), ('4', 'В планах'), ('5', 'Любимые')], max_length=255, verbose_name='вкладка'),
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
    ]
