from django.db import models

# Para el campo Document_type de la clase Person
class DocumentType(models.TextChoices):
    CC = "CEDULA DE CIUDADANIA"
    TD = "TARJETA DE IDENTIDAD"

class Person(models.Model):
    document_type = models.CharField(max_length=100, choices=DocumentType.choices, default=DocumentType.CC)
    document = models.CharField(max_length=100, unique=True)
    names = models.CharField(max_length=100)
    last_names = models.CharField(max_length=100)
    hobbie = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
