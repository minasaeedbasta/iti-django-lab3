from django.db import models
from authors.models import Author
from django.shortcuts import reverse,get_object_or_404

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete= models.CASCADE,null=True, related_name= 'books')
    price = models.IntegerField(default=10, null=True)
    no_of_pages = models.IntegerField(default=10, null=True)
    image = models.ImageField(upload_to='books/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"


    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_url(self):
        url = reverse('books.show', args=[self.id])
        return url
    
    @classmethod
    def get_book_by_id(cls, id):
        return get_object_or_404(cls, id=id)
