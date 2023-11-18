from django.shortcuts import render
from Mipagina.models import *
from Mipagina.forms import *
from django.http import HttpResponse

#////////////INDEX///////////////////////////////////////////////////////////


def inicio(request):
    return render(request,"Mipagina/index.html")


#////////////FORMULARIOS///////////////////////////////////////////////////////////

def cursoform(request):
    # Aca pregunta qué método es POST o GET
    if request.method == 'POST':
        curso_ok = Curso(nombre=request.POST['nombre'], camada=request.POST['camada'])  # Traigo del template los datos de los input
        curso_ok.save()
        return render(request, "Mipagina/index.html")

    return render(request, "Mipagina/cursoform.html")

def estudianteform(request):
    if request.method == 'POST':
        miformulario=EstudianteForm(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            info=Estudiante(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
            info.save()
            return render(request, "Mipagina/index.html")
    else:
        miformulario=EstudianteForm()   
    return render(request, "Mipagina/estudianteform.html",{'miformulario':miformulario})

def profesorform(request):
    if request.method == 'POST':
        miformulario=ProfesorForm(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            data=miformulario.cleaned_data
            data=Profesor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], edad=request.POST['edad'])
            data.save()
            return render(request, "Mipagina/index.html")
    else:
        miformulario=ProfesorForm()   
    return render(request, "Mipagina/profesorform.html",{'miformulario':miformulario})

#/////////////////////////////Buscadores///////////////////////////////////////////////////////

def buscar_camada(request):
    return render(request,"Mipagina/buscar_camada.html")    


def buscar(request):
    if 'camada' in request.GET:
        camada = request.GET['camada']

        if camada:
            cursos = Curso.objects.filter(camada__icontains=camada)

            if cursos:
                return render(request, 'Mipagina/resultadobusqueda.html', {'cursos': cursos, 'camada': camada})
            else:
                mensaje = f"No se encontraron cursos para la camada: {camada}"
                return render(request, 'Mipagina/error.html', {'mensaje': mensaje})
        else:
            mensaje = 'Por favor, ingresa un valor en el buscador.'
            return render(request, 'Mipagina/error.html', {'mensaje': mensaje})

    else:
        mensaje = 'No enviaste datos'
        return render(request, 'Mipagina/error.html', {'mensaje': mensaje})


    
   
    