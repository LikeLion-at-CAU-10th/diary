# Generated by Django 4.0.6 on 2022-08-02 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('diary_id', models.AutoField(primary_key=True, serialize=False)),
                ('foreign_key', models.CharField(max_length=200, verbose_name='일기외래키')),
                ('title', models.CharField(max_length=200, verbose_name='일기제목')),
                ('content', models.TextField(verbose_name='일기내용')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('weather', models.ImageField(upload_to='', verbose_name='날씨이모지')),
                ('feeling', models.ImageField(upload_to='', verbose_name='감정이모지')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('picture_id', models.AutoField(primary_key=True, serialize=False)),
                ('dot_count', models.IntegerField(verbose_name='점갯수')),
                ('picture_info', models.ImageField(upload_to='', verbose_name='일기그림')),
                ('order', models.IntegerField(verbose_name='점순서')),
            ],
        ),
        migrations.CreateModel(
            name='MemberPicture',
            fields=[
                ('member_picture_id', models.AutoField(primary_key=True, serialize=False)),
                ('picture_info', models.ImageField(upload_to='', verbose_name='선택한그림')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('uncolored_dot_info', models.CharField(max_length=200, verbose_name='아직안쓴점')),
                ('colored_dot_info', models.CharField(max_length=200, verbose_name='쓴점')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('picture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dot.picture')),
            ],
        ),
    ]
