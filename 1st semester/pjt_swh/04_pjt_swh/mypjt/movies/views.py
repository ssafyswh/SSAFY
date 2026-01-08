from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    

    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/create.html')


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        story = request.POST.get('story')
        director = request.POST.get('director')

        Movie.objects.create(
            title=title,
            story=story,
            director=director,
        )
        return redirect("movies:index")
    else:
        return render(request, "movies/create.html") 


def detail(request, id):
    movie = get_object_or_404(Movie, id=id)

    context = {
        'movie': movie,
    }

    return render(request, "movies/detail.html", context)


def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        story = request.POST.get('story')
        director = request.POST.get('director')
        
        movie.title = title
        movie.story = story
        movie.director = director   
        movie.save()

        return redirect("movies:detail", movie.id)
    else:
        context = {
            'movie' : movie,
        }
        return render(request, "movies/update.html", context)


def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('movies:index')