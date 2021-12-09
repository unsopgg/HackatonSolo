from django.db import models

from ..account.models import User
# from ..category.models import Category


class Manga(models.Model):
    STATUS_CHOICES = [
        ('ONGOING', 'ongoing'),
        ('FROZEN', 'frozen'),
        ('FINISHED', 'finished'),
    ]

    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manga', blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='manga')
    description = models.TextField()
    image = models.ImageField(upload_to='')
    author = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

class Saved(models.Model):
    user = models.ForeignKey(User, related_name='saved', on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, related_name='saved', on_delete=models.CASCADE)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.saved}'

class Like(models.Model):
    user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, related_name='like', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.like}'