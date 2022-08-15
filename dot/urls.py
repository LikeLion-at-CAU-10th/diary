# from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import TemplateView
from dot.views import *
import config
urlpatterns = [
  path('', pictures, name = 'picture_list') ,
  path('<int:id>', init_picture, name = 'init_picture'),
  path('diary/<int:diary_id>/<int:member_picture_id>', choosen_picture_get, name = 'choosen_picture_get'),
  path('update_diary/<int:diary_id>/<int:member_picture_id>', choosen_picture_patch, name = 'choosen_picture_patch'),    
  # path(r'^diary/(?P<int:diary_id>[0-9]+)/(?P<int:member_picture_id>[0-9]+)/$', choosen_picture, name = 'choosen_picture'),
  # path('<int:id>')
  # P<diary_id>[0-9]+/?P<member_picture_id>[0-9]+
  path('cherry', cherry, name='cherry'),
]
