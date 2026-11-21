def funcion_cantidad_espacio_muestral(lanzamientos):
    return 6**lanzamientos

n = int(input("Coloque el numero de lanzamientos del dado: "))

print(f"El numero de puntos muestrales es: {funcion_cantidad_espacio_muestral(n)}")