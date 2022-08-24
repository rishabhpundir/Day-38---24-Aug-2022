from django.db import models

MALE = 'M'
FEMALE = 'F'
UNKNOWN = 'U'
TYPE_CHOICES = (
(MALE, 'Male'),
(FEMALE, 'Female'),
(UNKNOWN, 'Unknown'),
)

class Singer(models.Model):
    singer_name = models.CharField(max_length=200)
    gender = models.CharField(choices=TYPE_CHOICES, max_length=20, default=UNKNOWN)

class Song(models.Model):
    song_title = models.CharField(max_length=200)
    from_movie = models.CharField(max_length=100)
    release_year = models.IntegerField()
    singer = models.ForeignKey(Singer, related_name='songs', on_delete=models.CASCADE)