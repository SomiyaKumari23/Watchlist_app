from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    #This movie is visible to users. if false means stored in db but hidden
    activate = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
