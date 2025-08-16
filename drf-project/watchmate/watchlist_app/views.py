from django.http import HttpResponse,JsonResponse,Http404
from watchlist_app.models import Movie

def movies_list(request):
    movies = Movie.objects.all()
    #return HttpResponse(movies)  # will print queryset as text
    #movies.values()=query set of dictionary
    data={'movies' : list(movies.values())}
    return JsonResponse(data)
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        raise Http404("Movie not found")
    
    data = {
        "name": movie.name,
        "description": movie.description,
    }
    return JsonResponse(data)