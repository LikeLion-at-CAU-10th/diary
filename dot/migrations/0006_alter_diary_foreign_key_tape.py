# Generated by Django 4.0.6 on 2022-08-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot', '0005_tape_remove_diary_tape_diary_foreign_key_tape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='foreign_key_tape',
            field=models.CharField(default='0', max_length=200, verbose_name='테입 외래키'),
        ),
    ]
