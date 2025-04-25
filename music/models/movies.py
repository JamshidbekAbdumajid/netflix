from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    year = models.IntegerField(blank=True,null=True)
    imdb = models.CharField(max_length=10, blank=True,null=True)
    genre = models.CharField(max_length=10)
    actors = models.ManyToManyField('music.Actor', related_name='movies')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movies'