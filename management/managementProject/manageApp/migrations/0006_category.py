# Generated by Django 3.2.1 on 2021-05-06 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0005_auto_20210505_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
