# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Region(models.Model):
    """
    Region object
    """
    codigo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Provincia(models.Model):
    """
    Provincia object
    """
    codigo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    region = models.ForeignKey('Region')

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Comuna(models.Model):
    """
    Comuna object
    """
    codigo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    provincia = models.ForeignKey('Provincia')

    def __str__(self):
        return self.nombre
