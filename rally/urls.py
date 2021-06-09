from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns=[
    path('',views.main,name = 'main'),
]