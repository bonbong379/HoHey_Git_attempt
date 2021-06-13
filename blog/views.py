from django.shortcuts import render
from .models import Post
from film.models import film_profile



# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def search_films(request):
    if request.method == "POST":
        searched = request.POST['searched']
        films = film_profile.objects.filter(film_name__contains = searched)
        return render(request, 'search_films.html', {'films': films})
    else:
        return render(request, 'search_films.html',  {})