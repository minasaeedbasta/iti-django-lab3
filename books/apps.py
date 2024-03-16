from django.apps import AppConfig

# this file contains config class of the application
class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'  # name of the application