from datetime import datetime
# from email.policy import default
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name =models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    
    
    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=300)
    date_released = models.DateField(default= datetime.today)
    LIKES_CHOICE=(
        ("Ls","likes"),
        ("dls","dislikes")
    )
    likes= models.CharField(choices=LIKES_CHOICE, max_length=3,null=True)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField(max_length=5000)
    Song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content