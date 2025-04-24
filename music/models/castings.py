from  django.db import models



class Casting(models.Model):
    actor = models.ForeignKey('music.Actor',on_delete=models.CASCADE)
    movie = models.ForeignKey('music.Movie',on_delete=models.CASCADE)
    role = models.CharField(max_length=10, blank=True,null=True)
    joined_at = models.DateField(blank=True,null=True)

