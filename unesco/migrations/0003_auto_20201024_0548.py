# Generated by Django 3.1.1 on 2020-10-24 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0002_auto_20201024_0539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iso',
            old_name='iso',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='region',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='state',
            new_name='name',
        ),
    ]