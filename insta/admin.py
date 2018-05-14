from django.contrib import admin
from .models import Profile, Comment, Like, Photo, Image
# Register your models here.

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Photo)
admin.site.register(Image)
