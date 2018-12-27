from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=30)
    count = models.PositiveIntegerField(default=1)
    searches = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Search')
    created_at = models.DateTimeField(auto_now_add=True)
    searched_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Search(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    searched_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Searches'

    def __str__(self):
        return self.tag.name


class Like(models.Model):
    image_url = models.CharField(max_length=120)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.image_url
