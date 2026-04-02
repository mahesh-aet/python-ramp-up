from django.db import models

# Create your models here.
class GeekModel(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
    

class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 
    release_date = models.DateField()
    num_stars = models.IntegerField()

