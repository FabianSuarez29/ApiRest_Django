from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class ApiDataCristian(models.Model):
    # Los campos que se extraen de la API
    descripcion = models.CharField(max_length=255)
    stock = models.IntegerField(null=True, blank=True)
    ubicacion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.descripcion} - {self.stock} - {self.ubicacion}"

class ApiDataAndres(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    technology = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.technology}"

class ApiDataCamila(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    technology = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.technology}"
    