from django.shortcuts import render, get_object_or_404
from .models import Post, Hashtag
from .forms import LoginForm, PostForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.conf import settings
import re

def find_hashtags(content: Post):
    hashtags = set(re.findall(r'#(\w+)', content.text))
    for c in hashtags:
        hashtag_obj, created = Hashtag.objects.get_or_create(name = c)
        content.hashtags.add(hashtag_obj)

def index(request):
    posts = Post.objects.order_by('-creation_date')
    user = request.user
    context = {'posts': posts, 'user': user}
    return render(request, 'index.html', context = context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()   
    context = {'form': form}
    return render(request, 'login.html', context)   

def post_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(text = form.cleaned_data.get('text'), author = request.user)
            find_hashtags(post)

            return redirect('index')      
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'post.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            if form.cleaned_data.get('password') == form.cleaned_data.get('confirm_password'):
                password = form.cleaned_data.get('password')
            elif form.cleaned_data.get('password') != form.cleaned_data.get('confirm_password'):
                form.add_error('confirm_password', 'The passwords are not the same.')
            email = form.cleaned_data.get('email')
            user = get_user_model()
            user.objects.create_user(username = username, email = email, password = password)
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def user_profile(request, username):
    user = get_object_or_404(get_user_model(), username = username)
    context = {'user': user, 'posts':Post.objects()}
    return render(request, 'user.html', context)


def filter_by_hashtags(request, hashtag):
    if hashtag:
        try:
            hashtag_obj = Hashtag.objects.get(name = hashtag)
            posts = hashtag_obj.posts.all()
            context = {'posts': posts}
        except:
            posts = Post.objects.none()
        
        return render(request, 'hashtags.html', context)

            

    


