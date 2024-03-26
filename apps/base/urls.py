from django.urls import path
from apps.base.views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('about_us/', about_us, name='about_us_url'),
    path('team/', team, name='team_url'),
    path('post/', post, name='post_url'),
    path('news/', news, name='news_url'),
    path('gallery/', gallery, name='gallery_url'),
    path('contact/', contact, name='contact_url'),
]