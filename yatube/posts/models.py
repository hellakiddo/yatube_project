from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Group(models.Model):
    title = models.TextField()
    slug = models.SlugField(default='some string')
    description = models.CharField(max_length=10000, default='some string')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, blank=True, null=True,
                              on_delete=models.CASCADE,
                              related_name='posts')
