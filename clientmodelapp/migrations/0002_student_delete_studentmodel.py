# Generated by Django 4.0.4 on 2022-08-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientmodelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentModel',
        ),
    ]
