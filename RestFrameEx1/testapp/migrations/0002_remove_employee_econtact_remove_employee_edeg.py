# Generated by Django 5.0.6 on 2024-05-24 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='econtact',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='edeg',
        ),
    ]
