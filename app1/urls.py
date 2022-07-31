from django.urls import re_path
from app1.views import  home
urlpatterns = [
    re_path('', home,name='home'),
]
