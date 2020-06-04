from django.shortcuts import render
#importando mi formulario
from appregistro.forms import RegistroForm

from django.shortcuts import redirect

from appregistro.models import Registro


# Create your views here.
def inicio(request):
    form=RegistroForm()
    registro=Registro.objects.all()

    return render(request, "index.html", {"form":form, 'registro':registro})


def registrar(request):

    if request.method=='POST':
       form=RegistroForm(request.POST)
       if form.is_valid:
        form.save()
        
        return render(request,"registroexitoso.html")
    else:
        form=RegistroForm()

        return render(request, "registrarusuario.html", {'form':form})   

def mostrarregistros(request):

    registro=Registro.objects.all()

    form=RegistroForm()

    return render(request, "registrousuarios.html", {'registro':registro, 'form':form})

def eliminarregistro(request):
    if request.POST["id1"]:

        form=request.POST["id1"]

        registro=Registro.objects.filter(id=form) 
        registro.delete()
        return render(request, "eliminado.html") 
    else :
       registro=Registro.objects.all()

       return render(request, "registrousuarios.html", {'registro':registro}) 

def eliminar(request):
    registro=Registro.objects.all()

    return render(request, "eliminar.html", {'registro':registro})       



def actualizar1(request):
    registro=Registro.objects.all()


    return  render(request, "actualizar1.html", {'registro':registro})
   

         

def actualizar(request,items_id):
    #creando una instancia para pasarle los datos del registro al formulario y despues actualizarlos
    instancia=Registro.objects.get(id=items_id)
    form=RegistroForm(instance=instancia)

    if request.method=="POST":
        
        form=RegistroForm(request.POST, instance=instancia)

        if form.is_valid():
            #funcion para actualizar el registro despues se vuelve a crear una instancia del formulario para limpiar el registro  
            instancia.save()

            form=RegistroForm()
        #si el registro es exitoso se le redirecciona a una vista que confirma la actualizacion como exitosa
        return render(request, "editar.html", {'form': form})        
    else :
        instancia=Registro.objects.get(id=items_id)

        form=RegistroForm(instance=instancia)
        
        return render(request, "actualizar.html", {'form': form}) 


   


    
