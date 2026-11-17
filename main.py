from generador import crear_laberinto
from algoritmos import dijkstra

def main():

    print("=== PROYECTO LABERINTO ===")

    filas, columnas = 11,11
    laberinto = crear_laberinto(filas, columnas)

    #Definir el inicio y el fin
    inicio = (1,1)
    fin =(filas -2, columnas-2) #Esquina Inferior derecha interna

    print(f"Inicio: {inicio} | Fin: {fin}\n")

    # Ejecutar Dijkstra
    ruta, costo, explorados = dijkstra(laberinto, inicio, fin)
    print(f"Ruta optima encontrada: {len(ruta)} pasos.")
    print(f"Costo total: {costo}.")
    print(f"Nodos explorados {explorados}\n")

    #Visualizacion en consola marcando la ruta con *
    for f in range(filas):
         linea = ""
         for c in range(columnas):
              if (f,c )== inicio:
                   linea += "S " #Start
              elif(f,c)== fin:
                   linea += "E " #End
              elif(f,c) in ruta :
                   linea += "* " #Ruta Optima
              elif laberinto[f][c] ==1:
                   linea += "██" #PAared
              else :
                   linea += " " #Espacio libre
         print(linea)
    
    

if __name__ == "__main__":
        main()