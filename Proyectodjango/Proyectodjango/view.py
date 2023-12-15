#"Esta carpeta view se crea para crear las funciones o las partes visibles de la pag"

from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola papa, es el inicio de una pag web")

#Funcion con parametros pasados directamente de python que se muestran en la vistas
def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)

#Funcion con parametros pasados desde la URL cuando estamos en el navegador

def miNombreEs(self, nombre):
    documento_de_texto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documento_de_texto)

