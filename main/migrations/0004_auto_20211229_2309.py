# Generated by Django 3.2.9 on 2021-12-29 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211229_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jelo',
            name='slika',
            field=models.ImageField(default='static/img/default1.jpg', upload_to='static/user/'),
        ),
        migrations.AlterField(
            model_name='restoran',
            name='slika',
            field=models.ImageField(default='static/img/default1.jpg', upload_to='static/user/'),
        ),
    ]