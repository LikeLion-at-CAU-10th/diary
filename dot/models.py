from tabnanny import verbose
from django.db import models
from django.forms import CharField
from accounts.models import User
# Create your models here.


class Picture(models.Model):
    picture_id = models.AutoField(primary_key=True)
    dot_count = models.IntegerField(verbose_name='점갯수')
    picture_info = models.ImageField(verbose_name='일기그림')
    order = models.IntegerField(verbose_name='점순서')
    picture_complete_info = models.ImageField(verbose_name = "다한그림", null = True)

class MemberPicture(models.Model):
    member_picture_id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, blank=False)
    picture_id = models.ForeignKey(
        to=Picture, on_delete=models.CASCADE, blank=False)
    picture_info = models.ImageField(verbose_name='선택한그림')
    create_date = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    uncolored_dot_info = models.CharField(verbose_name="아직안쓴점", max_length=200)
    colored_dot_info = models.CharField(verbose_name="쓴점", max_length=200)
    diary_id=models.CharField(verbose_name="일기아이디",max_length=200, null=True,blank=True)
class Tape(models.Model):
    tape_id = models.AutoField(primary_key= True)
    tape_info = models.ImageField(verbose_name= "tape")
class Diary(models.Model):
    diary_id = models.AutoField(primary_key=True)
    foreign_key = models.CharField(verbose_name='일기외래키', max_length=200)
    foreign_key_tape = models.CharField(verbose_name = "테입 외래키", max_length = 200, default = "0")
    title = models.CharField(verbose_name='일기제목', max_length=200)
    content = models.TextField(verbose_name='일기내용')
    create_date = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    
    updated_date = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    weather = models.ImageField(verbose_name='날씨이모지')
    feeling = models.ImageField(verbose_name='감정이모지')
    
