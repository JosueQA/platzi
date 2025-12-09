from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=15, null=True)

    def __str__(self):
        return f"{self.title} - {self.year}"

class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Autor(models.Model): # Nuevo modelo
    nombre = models.TextField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.nombre

class Profile(models.Model):
    website = models.URLField()
    biography = models.TextField(max_length=500)
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE)   

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Autor, related_name='books') # Nuevo campo

    def __str__(self):
        return self.title