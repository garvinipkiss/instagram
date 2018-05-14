from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Profile, Photo, Comment
from django.contrib.auth.models import User
from .forms import NewPhotoForm, EditProfileForm, AddCommentForm, EditUserForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.urlresolvers import reverse



# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    posts = Photo.get_photos()
    return render(request, 'index.html', {"current_user": current_user, "posts": posts})


@login_required(login_url='/accounts/login/')
def userprofile(request, user_id):
    try:
        profile = Profile.objects.filter(id=user_id)
        photos = Photo.objects.filter(user_id=user_id)
    except Photo.DoesNotExist:
        raise Http404()
    return render(request, 'userprofile.html', {"profile": profile, "photos": photos})

def followers(request, username):
  user = user = User.objects.get(username = username)
  user_profile = Profile.objects.get(user=user)
  profiles = user_profile.followers.all

  title = "Followers"

  return render(request, 'follow_list.html', {"title": title, "profiles":profiles})

def following(request, username):
  user = user = User.objects.get(username = username)
  user_profile = Profile.objects.get(user=user)
  profiles = user_profile.following.all()

  title = "Following"

  return render(request, 'follow_list.html', {"title": title, "profiles":profiles})

@login_required(login_url='/accounts/login/')
def explore(request):
    '''
    function to display the index page
    '''
    image = Image.objects.all()
    return render(request, 'explore.html', {"image": image})

@login_required(login_url='/accounts/login/')
def explore(request, image_id):

    image = Image.objects.get(id=image_id)

    return render(request, 'explore.html', {"image": image})
@login_required(login_url='/accounts/login/')
def search(request):
    if 'profile' in request.GET and request.GET['profile']:
            search_term = request.GET.get('profile')
            searched_photos = Profile.search_profile(search_term)
            message = f"{search_term}"

            return render(request, 'search.html', {"message": message, "posts": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def photo(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = current_user
            photo.save()
            return redirect('index')
    else:
        form = NewPhotoForm()
    return render(request, 'photo.html', {"form": form})


@login_required(login_url='/accounts/login/')
@transaction.atomic
def edition(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('index')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
    return render(request, 'edition.html', {"user_form": user_form, "profile_form": profile_form})


@login_required(login_url='/accounts/login/')
def comment(request, id):
    title = 'Instagram | Comment'
    post = get_object_or_404(Photo, id=id)
    current_user = request.user
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.photo = post
            comment.save()

            return redirect('index')
    else:
        form = AddCommentForm()

    return render(request, 'comment.html', {"title": title, "form": form})
