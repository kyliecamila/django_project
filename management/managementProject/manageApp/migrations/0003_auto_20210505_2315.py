# Generated by Django 3.2.1 on 2021-05-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0002_post_memo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.CharField(default='몰라', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='memo',
            field=models.TextField(default='메모 없음'),
        ),
    ]