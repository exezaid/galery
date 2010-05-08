from django.shortcuts import render_to_response
from models import Photo

def view_photos(request):
    photo_list = Photo.objects.order_by('-date')[:10]
    return render_to_response('latest_photos.html', {'photo_list': photo_list})
