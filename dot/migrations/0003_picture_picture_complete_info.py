# Generated by Django 4.0.6 on 2022-08-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot', '0002_memberpicture_diary_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='picture_complete_info',
            field=models.ImageField(null=True, upload_to='', verbose_name='다한그림'),
        ),
    ]
