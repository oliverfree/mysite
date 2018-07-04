from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from slugify import slugify


class Image(models.Model):
    user = models.ForeignKey(User, related_name='images')
    title = models.CharField(max_length=300)
    url = models.URLField(max_length=280)
    slug = models.SlugField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    # create index on table(created)
    created = models.DateField(auto_now_add=True, db_index=True)
    # django upload_to built-in strftime function
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)