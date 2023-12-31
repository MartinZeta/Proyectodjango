from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "core/index.html", {"nombre": "Ferretería"})

#def probando_template(request):
#    nombre = "Martin"
#    apellido = "Avelen"
#    diccionario = {"nombre": nombre, "apellido": apellido} #<---------------- Para enviar al contexto
#    mi_html = open("./templates/core/index.html")
#    plantilla = Template(mi_html.read())
#    mi_html.close()
#    mi_contexto = Context(diccionario)
#    documento = plantilla.render(mi_contexto)
#    return HttpResponse(documento)