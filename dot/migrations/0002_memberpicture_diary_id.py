# Generated by Django 4.0.6 on 2022-08-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberpicture',
            name='diary_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='일기아이디'),
        ),
    ]
