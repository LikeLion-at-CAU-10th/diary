<<<<<<< HEAD
# Generated by Django 4.1 on 2022-08-19 14:45
=======
# Generated by Django 4.0.6 on 2022-08-19 15:11
>>>>>>> d63c3a4ed5398d52d805834a78cee4953412c0c3

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ("dot", "0006_alter_diary_foreign_key_tape"),
=======
        ('dot', '0006_alter_diary_foreign_key_tape'),
>>>>>>> d63c3a4ed5398d52d805834a78cee4953412c0c3
    ]

    operations = [
        migrations.AlterField(
<<<<<<< HEAD
            model_name="diary",
            name="foreign_key_tape",
            field=models.CharField(default="1", max_length=200, verbose_name="테입 외래키"),
=======
            model_name='diary',
            name='foreign_key_tape',
            field=models.CharField(default='1', max_length=200, verbose_name='테입 외래키'),
>>>>>>> d63c3a4ed5398d52d805834a78cee4953412c0c3
        ),
    ]
