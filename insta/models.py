from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    prof_pic = models.ImageField(upload_to='profile/', null=True, blank=True)
    bio = models.TextField(max_length=140)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('Profile', related_name = 'followers_profile', blank =True)
    following = models.ManyToManyField('Profile', related_name='following_profile', blank =True)
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, id, bio):
        update = Photo.objects.filter(id=id).update(bio=bio)
        return update

    @classmethod
    def search_profile(cls, search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def get_profiles(cls):
        profiles = Profile.objects.all()
        return profiles


class Like(models.Model):
    like = models.IntegerField(default=0)

    def __int__(self):
        return self.like

    def save_like(self):
        self.save()

    def delete_like(self):
        self.delete()


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    photo_caption = models.CharField(max_length=140)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.profile

    def save_photo(self):
        self.save()

    @classmethod
    def get_photos(cls):
        photos = Photo.objects.all()
        return photos

class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='photos/', null="True", blank="True")

    # __str__ will return string representation of the image model
    # __str__ will enable us view our returned queries

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Comment(models.Model):
    comment = models.CharField(max_length=140, null=True, blank=True)
    time_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comment', blank=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
