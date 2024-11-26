from django.contrib import admin
from django.urls import path
from x.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login_view, name = 'login'),
    path('post/', post_view, name = 'post'),
    path('register/', register_view, name = 'register_view'),
    path('user/<str:username>/', user_profile, name = 'profile_view'),
    path('hashtags/<str:hashtag>', filter_by_hashtags, name = 'hashtags')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)