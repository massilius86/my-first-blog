from django.conf import settings
from django.db import models
from django.utils import timezone


# Defining my Post model
class Post(models.Model):  # models.Model means that the Post is a Django Model,
                           # so Django knows that it should be saved in the database.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
