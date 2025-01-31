from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Submenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title