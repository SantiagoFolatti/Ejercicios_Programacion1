def ordenar_array(lista, descendente = False):
    for i in range(0, len(lista) -1):
        for j in range (i+1, len(lista), 1):
            if lista[i] > lista[j] and not descendente: #CRITERIO DE ORDENAMiENTO
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar  
                
            elif lista[i] < lista[j] and descendente: #CRITERIO DE ORDENAMiENTO
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    
    return lista           

lista = [5,1,9,8,3,2]
resultado_ordenar_array = ordenar_array(lista,True)
# print(resultado_ordenar_array)
