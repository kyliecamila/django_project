# Generated by Django 3.2.1 on 2021-05-05 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='compleeted',
            new_name='completed',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='iteem',
            new_name='item',
        ),
    ]