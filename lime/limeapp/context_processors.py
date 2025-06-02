from .models import Song

# NOT CURRENTLY IN USE, USED TO PASS THE SONG OBJECT TO BASE.HTML

def song_list(request):
    return {
        'songs': Song.objects.all()
    }