from operator import mod
from pyexpat import model
from tabnanny import verbose
from turtle import title
from django.db import models
from django.forms import CharField

# Create your models here.


class Picture(models.model):
    picture_id = models.AutoField(primary_key=True)
    dot_count = models.IntegerField(verbose_name='점갯수', max_length=30)
    picture_info = models.ImageField(verbose_name='일기그림')
    order = models.IntegerField(verbose_name='점순서')

# class Dot(models.model):
#     dot_id=models.AutoField(primary_key=True)
#     picture_id=models.ForeignKey(to=Picture, on_delete=models.CASCADE, blank=False)
#     x=models.IntegerField(verbose_name='점의x좌표')
#     y=models.IntegerField(verbose_name='점의y좌표')


class MemberPicture(models.model):
    member_picture_id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(
        to=Memeber, on_delete=models.CASCADE, blank=False)
    picture_id = models.ForeignKey(
        to=Picture, on_delete=models.CASCADE, blank=False)
    picture_info = models.ImageField(verbose_name='선택한그림')
    create_date = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    uncolored_dot_info = models.CharField(verbose_name="아직안쓴점")
    colored_dot_info = models.CharField(verbose_name="쓴점")


class Diary(models.model):
    diary_id = models.AutoField(primary_key=True)
    foreign_key = models.CharField(verbose_name='일기외래키')
    title = models.CharField(verbose_name='일기제목', max_length=200)
    content = models.TextField(verbose_name='일기내용')
    create_date = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    weather = models.ImageField(verbose_name='날씨이모지')
    feeling = models.ImageField(verbose_name='감정이모지')
