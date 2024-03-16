from django.db import models
from django.shortcuts import reverse,get_object_or_404

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/images/', null=True)
    bdate = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"


    @property
    def image_url(self):
        return f'/media/{self.image}'


    @property
    def show_url(self):
        url = reverse('authors.show', args=[self.id])
        return url
    
    @classmethod
    def get_author_by_id(cls, id):
        return get_object_or_404(cls, id=id)
