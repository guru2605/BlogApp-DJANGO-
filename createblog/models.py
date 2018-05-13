from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class NewPost(models.Model):
    post_name = models.CharField(max_length=30)
    post_text = models.CharField(max_length=5000)
    def __str__(self):
        return self.post_name
