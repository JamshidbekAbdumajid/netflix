from django.db import  models
from django.contrib.auth import get_user_model
from music.models import Movie

User = get_user_model()

class Commit(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='commits')
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='movies')
    text = models.TextField(max_length=120)
    created_date = models.DateTimeField(null=True,blank=True, auto_now_add=True)
