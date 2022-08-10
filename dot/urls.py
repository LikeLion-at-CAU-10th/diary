# from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import TemplateView
from dot.views import *
import config
urlpatterns = [
  path('', pictures, name = 'picture_list') ,
  # path('<int:id>')
  path('practice/', practice),
]

