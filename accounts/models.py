from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import *

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length = 10, 
        unique = True, 
        null = True,
        validators=[validate_no_special_characters],
        error_messages={"unique": "이미 사용중인 닉네임입니다."})
<<<<<<< HEAD
    profile = models.ImageField(null = True,default = "Profile.svg")
    picture_list = models.CharField(max_length = 200, default = "1 2 3 4 5")
    
=======
    profile = models.ImageField(null = True)
    picture_list = models.CharField(max_length = 200, default = "1 2 3 4")
>>>>>>> 4d6f708 (gwgw)
    def __str__(self):
        return self.email
