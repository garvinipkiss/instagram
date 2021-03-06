from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^photo/', views.photo, name='photo'),
    url(r'^edition/', views.edition, name='edition'),
    url(r'^explore/(\d+)', views.explore, name='explore'),
    url(r'^userprofile/(\d+)', views.userprofile, name='userprofile'),
    url(r'^profile/(?P<username>[-_\w.]+)/followers/$', views.followers, name='followers'),
    url(r'^profile/(?P<username>[-_\w.]+)/following/$', views.following, name='following'),
    url('^comment/(?P<id>\d+)', views.comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
