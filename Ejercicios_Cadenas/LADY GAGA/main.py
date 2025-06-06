from datetime import date
datos = {
    "Tema" : "Bradley Cooper | Lukas Nelson - Shallow",
    "Vistas" : "1900 millones",
    "Duracion" : "3:37",
    "Link" : "https://www.youtube.com/watch?v=bo_efYhYU2A",
    "Fecha de Lanzamiento" : "2018-09-27"
}

def obtener_colaboradores(titulo:str) -> list:
    lista = titulo.split(" - ")
    colaboradores = lista[0].split(" | ")
    return colaboradores

def obtener_nombre_tema(titulo: str) -> str:
    lista = titulo.split(" - ")
    nombre_real = lista[1]
    return nombre_real

def convertir_vistas_numerico(vistas: str) -> int:
    if "millones" in vistas:
        numero_str = vistas.replace("millones","").strip()
        numero = int(numero_str)
        return numero * 1000000

def convertir_duracion_numerico(duracion: str) -> int:
    duracion = duracion.split(":")
    numero_1 = int(duracion[0])
    numero_2 = int(duracion[1])
    
    total_duracion = numero_1 * 60 + numero_2
    return total_duracion

def obtener_codigo(url: str) -> str:
    lista = url.split("=")
    url = lista[1]
    return url

def formatear_fecha(fecha: str) -> date:
    lista = fecha.replace("-","/")
    return lista
    
def mostrar(mensaje,valor):
    print(mensaje,valor)

colaboradores = obtener_colaboradores(datos["Tema"])
nombre_real = obtener_nombre_tema(datos["Tema"])
vistas_numerico = convertir_vistas_numerico(datos["Vistas"])
duracion = convertir_duracion_numerico(datos["Duracion"])
url = obtener_codigo(datos["Link"])
fecha = formatear_fecha(datos["Fecha de Lanzamiento"])

mostrar("Colaboradores :",colaboradores)
mostrar("Nombre del tema :",nombre_real)
mostrar("vistas :",vistas_numerico)
mostrar("Duración :",duracion)
mostrar("Fecha :",fecha)


