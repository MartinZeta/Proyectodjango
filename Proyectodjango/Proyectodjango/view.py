#"Esta carpeta view se crea para crear las funciones o las partes visibles de la pag"

from django.http import HttpResponse
import datetime
import random

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

#-------------------------------------------------

# Crear una función que solicite mi nombre
# y la muestre en pantalla al ingresar a una url
# diferente a 'saludo'

def ingresar_nombre(request) -> HttpResponse:
    nombre = input('Ingresa tu nombre: ')
    return HttpResponse(f'Hola <h1>{nombre}</h1>, como estas?')

#-------------------------------------------------

##Otra funcion con fecha y hora

def fecha_hora(request):
    ahora = datetime.datetime.now().strftime(r"%d/%m/%Y  %H:%M:%S.%f")
    return HttpResponse(ahora)

#--------------------------------------------------

# Crear una vista que muestre "Has tirado el dado: <numero>"
# Si el número es 6, mostrar una felicitación
# Si no, mostrar que vuelva a intentar
# import random
# randint(1, 6)

def tirar_dado(request):
    numero = random.randint(1,6)
    if numero == 6:
        return HttpResponse(f' <h1> Tiraste el dado: 🎲 {numero} ✨')
    else: 
        return HttpResponse(f' <h1> Tiraste el dado: 🎲 {numero} </h1> <br> Volve a intentarlo! 🥺')

