# Generated by Django 4.0.6 on 2022-08-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot', '0006_alter_diary_foreign_key_tape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='foreign_key_tape',
            field=models.CharField(default='1', max_length=200, verbose_name='테입 외래키'),
        ),
    ]
