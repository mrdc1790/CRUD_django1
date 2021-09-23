from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'AdamP',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 23, 2021'
    },
    {
        'author': 'JaneDoe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 23, 2021'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})