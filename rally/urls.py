from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns=[
    path('',views.main,name = 'main'),
    path('details/<str:pk>/',views.details,name = 'details'),
    path('profile/<username>/',views.profile,name = 'profile'),
    path('edit_profile/',views.edit_profile,name = 'edit_profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('create_post/',views.create_post,name = 'create_post'),
    re_path('comment/(?P<post_id>\d+)', views.comment, name='comment'),
    path('welcome/', views.welcome_mail, name='welcome'),
    path('register',views.register,name = 'register'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)