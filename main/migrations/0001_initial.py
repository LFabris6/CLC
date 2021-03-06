# Generated by Django 3.2.9 on 2021-12-12 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(blank=True, max_length=50)),
                ('prezime', models.CharField(blank=True, max_length=50)),
                ('telefon', models.IntegerField(max_length=20, null=True)),
                ('adresa', models.CharField(blank=True, max_length=50)),
                ('sirina', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('duzina', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('regija', models.CharField(blank=True, max_length=50)),
                ('grad', models.CharField(blank=True, max_length=50)),
                ('drzava', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
