from django.db import models
from django.shortcuts import render



class Curso(models.Model):
        nombre=models.CharField(max_length=40)
        camada=models.IntegerField()
        
class Estudiante(models.Model):
        nombre=models.CharField(max_length=30)
        apellido=models.CharField(max_length=30)
        email=models.EmailField()

class Profesor(models.Model):
        nombre=models.CharField(max_length=30)
        apellido=models.CharField(max_length=30)
        email=models.EmailField()
        edad=models.IntegerField()





