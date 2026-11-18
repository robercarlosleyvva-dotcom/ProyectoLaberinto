from generador import crear_laberinto
from algoritmos import dijkstra

def main():

    print("=== PROYECTO LABERINTO ===")

    # Dimensiones impares obligatorias para que la cuadrícula cierre perfecta
    filas, columnas = 11, 11
    laberinto = crear_laberinto(filas, columnas)

    # Definir el inicio
    inicio = (1, 1)
    
    # Búsqueda dinámica: encontrar la última celda transitable (0) cerca de la esquina inferior derecha
    fin = None
    for f in range(filas - 2, 0, -1):
        for c in range(columnas - 2, 0, -1):
            if laberinto[f][c] == 0:
                fin = (f, c)
                break
        if fin:
            break
            
    # Respaldo por seguridad si no encuentra ninguna
    if not fin:
        fin = (filas - 2, columnas - 2)

    print(f"Inicio: {inicio} | Fin: {fin}\n")

    print("Valor en inicio:" , laberinto[inicio[0]][inicio[1]])
    print("Valor en fin: ", laberinto[fin[0]][fin[1]])


    # Ejecutar Dijkstra
    ruta, costo, explorados = dijkstra(laberinto, inicio, fin)
    print(f"Ruta óptima encontrada: {len(ruta)} pasos.")
    print(f"Costo total: {costo}.")
    print(f"Nodos explorados: {explorados}\n")

    # Visualización en consola marcando la ruta con *
    for f in range(filas):
         linea = ""
         for c in range(columnas):
              if (f, c) == inicio:
                   linea += "S " # Start
              elif (f, c) in ruta and (f, c) == fin:
                   linea += "* " # Si la ruta pasa por el fin, cerramos con asterisco
              elif (f, c) == fin:
                   linea += "E " # End
              elif (f, c) in ruta:
                   linea += "* " # Ruta Óptima
              elif laberinto[f][c] == 1:
                   linea += "██" # Pared
              else:
                   linea += "  " # Espacio libre
         print(linea)

if __name__ == "__main__":
        main()