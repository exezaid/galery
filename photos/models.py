from django.db.models import *

class Photo(Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to="photo_images")
    date = DateTimeField()
    class Admin:
        pass
