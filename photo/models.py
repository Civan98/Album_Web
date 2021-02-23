from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null= False, blank=False)
    class Meta:
        ordering = ['name',]#para ordenar alfabeticamente


    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    #image = models.ImageField(null=False, blank = False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.TextField()
    link = models.CharField(max_length=200, null= True, blank= True)

    def __str__(self):
        return self.description
