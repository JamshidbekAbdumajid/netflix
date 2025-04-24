from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    birth_date = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=10, blank=True,null=True)
    def __str__(self):
        return self.name