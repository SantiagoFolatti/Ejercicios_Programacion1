def encontrar_productos(usuario_1, usuario_2):
    productos_iguales = []
    for i in range(len(usuario_1)):
        for j in range(len(usuario_2)):   
            if usuario_1[i] == usuario_2[j]:
                productos_iguales = productos_iguales + [usuario_1[i]]
                break
    return productos_iguales

def diferencia_simetrica(usuario_1, usuario_2):
    diferencia_usuario_1 = []
    diferencia_usuario_2 = []
    for i in range(len(usuario_2)):
        esta = False
        for j in range(len(usuario_1)):
            if usuario_2[i] == usuario_1[j]:
                esta = True
                break
        if esta == False:
            diferencia_usuario_1 = diferencia_usuario_1 + [usuario_2[i]]
            
    for i in range(len(usuario_1)):
        esta = False
        for j in range(len(usuario_2)):
            if usuario_1[i] == usuario_2[j]:
                esta = True
                break
        if esta == False:
            diferencia_usuario_2 = diferencia_usuario_2+ [usuario_1[i]]
    
    return diferencia_usuario_1,diferencia_usuario_2

def catalogo_total(usuario_1,usuario_2):
    catalogo = usuario_1 
    for i in range(len(usuario_2)):
        for j in range(len(catalogo)):
            if usuario_2[i] == catalogo[j]:
                break
        else:
            catalogo = catalogo + [usuario_2[i]]

    return catalogo

def recomendacion (usuario_1, usuario_2):
    lista_recomendacion = diferencia_simetrica(usuario_1,usuario_2)
    return lista_recomendacion


usuario_1 = ["teclado","mouse","monitor","gabinete","procesador"]
usuario_2 = ["teclado", "auriculares", "monitor", "micrófono", "notebook"]  

resultado_productos_iguales = encontrar_productos(usuario_1,usuario_2)
resultado_diferencia= diferencia_simetrica(usuario_1,usuario_2)
resultado_catalogo = catalogo_total(usuario_1,usuario_2)
resultado_recomendacion = recomendacion(usuario_1, usuario_2)


print(f"\nProductos en comun: {resultado_productos_iguales}")
print(f"\nProductos exclusivos del usuario 1: {resultado_diferencia[1]}")
print(f"Productos exclusivos del usuario 2: {resultado_diferencia[0]}")
print(f"\nEL catalogo es: {resultado_catalogo}")
print(f"\nRecomendaciones para usuario 1: {resultado_recomendacion[0]}")
print(f"Recomendaciones para usuario 2: {resultado_recomendacion[1]}")

