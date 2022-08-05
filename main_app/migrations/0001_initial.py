# Generated by Django 4.1 on 2022-08-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]