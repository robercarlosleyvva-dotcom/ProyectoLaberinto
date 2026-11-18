from generador import crear_laberinto
from algoritmos import dijkstra

def main():

    print("=== PROYECTO LABERINTO ===")

    # Dimensiones fijas de 15x15
    filas, columnas = 15, 15
    laberinto = crear_laberinto(filas, columnas)

    # Definir inicio y fin de forma fija y segura en la esquina interior
    inicio = (1, 1) #Representa a 'S'  donde arranca el recorrido
    fin = (filas - 2, columnas - 2)  #  Representa a 'E'. Coordenadas (13, 13) en una matriz de 15x15

    # Fuerza que la meta y sus accesos sean 100% transitables para Dijkstra
    laberinto[fin[0]][fin[1]] = 0
    laberinto[fin[0] - 1][fin[1]] = 0  # Celda superior libre
    laberinto[fin[0]][fin[1] - 1] = 0  # Celda izquierda libre

    print(f"Inicio: {inicio} | Fin: {fin}\n")

    # Ejecutar Dijkstra
    # Ruta: Devuelve una lista con las coordenadas exactas (f,c) que forman el camino optimo
    #Costo: El peso total acomulado para llegar del inicio al fin.
    #Explorados: Cuantos nodos analizo el algoritmo en total

    ruta, costo, explorados = dijkstra(laberinto, inicio, fin)
    print(f"Ruta óptima encontrada: {len(ruta)} pasos.")
    print(f"Costo total: {costo}.")
    print(f"Nodos explorados: {explorados}\n")

    # Visualización en consola con la salida 'E' asegurada
    #Recorre celda por celda toda la matriz usando dos ciclos for anidados para armar renglon
    #por renglon un string (linea) que se imprime en pantalla
    for f in range(filas):
         linea = ""
         for c in range(columnas):
              if (f, c) == inicio:
                   linea += "S " # Start (inicio, punto de partida)
              elif (f, c) == fin:
                   linea += "E " # End (salida)
              elif (f, c) in ruta:
                   linea += "* " # Ruta Óptima
              elif laberinto[f][c] == 1:
                   linea += "██" # Pared
              else:
                   linea += "  " # Espacio libre
         print(linea)

#Es el estandar en python para indicar que si este archivo se ejecuta directamente desde 
#La terminal, llame a la funcion main() para arrancar el programa
if __name__ == "__main__":
        main()