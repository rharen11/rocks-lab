# Generated by Django 4.1 on 2022-08-07 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rock_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rock',
            old_name='painting',
            new_name='paintings',
        ),
    ]