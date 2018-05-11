from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^newphoto/', views.new_photo, name='new_photo'),
    url(r'^edition/', views.editprofile, name='edition'),
    url(r'^profile/(\d+)', views.user_profile, name='profile'),
    url('^comment/(?P<id>\d+)', views.comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
