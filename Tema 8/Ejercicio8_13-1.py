def recortar(t):
    """
    Modifica la lista original in-place eliminando
    el primer y el último elemento. Retorna None.
    """
    if len(t) >= 2:
        del t[-1]  
        del t[0]   
    elif len(t) == 1:
        del t[0]
    return None


def medio(t):
    """
    Crea y retorna una nueva lista con todo excepto
    el primer y el último elemento. No modifica la original.
    """
    return t[1:-1]

# 1. Prueba de recortar()
lista_a = [10, 20, 30, 40, 50]
resultado_recortar = recortar(lista_a)

print("--- Función recortar() ---")
print("Retorno de la función:", resultado_recortar)  
print("Lista original modificada:", lista_a)          

# 2. Prueba de medio()
lista_b = ["a", "b", "c", "d", "e"]
nueva_lista = medio(lista_b)

print("\n--- Función medio() ---")
print("Nueva lista retornada:", nueva_lista)           
print("Lista original intacta:", lista_b)             