from django.urls import path
from Mipagina.views import *
from Mipagina.models import *





urlpatterns = [
   
  path('',inicio, name='inicio'),
  path('curso/', cursoform, name='curso'),
  path('profesores/',profesorform, name='profesores'),
  path('estudiantes/',estudianteform, name='estudiantes'),
  path('buscarcamada/',buscar_camada, name='buscarcamada' ),
  path('buscarcamada/buscar/',buscar,name='buscar'),
  
]
