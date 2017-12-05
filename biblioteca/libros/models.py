# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from .validators import validate_content

# Create your models here.


class Libros(models.Model):

    Nombre = models.CharField(max_length=140, validators=[validate_content])
    Autor = models.CharField(max_length=200, validators=[validate_content])
    Editorial = models.CharField(max_length=400, validators=[validate_content])
    ISBN = models.CharField(max_length=250, validators=[validate_content])
    Precio = models.FloatField(validators=[validate_content])
    Creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nombre
