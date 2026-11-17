import random

def obtener_vecinos(fila,columna,filas,columnas):
     movimientos = [
          (-2,0), #Arriba
          (2,0), #Abajo
          (0,-2), #Izquierda
          (0,2) #Derecha
     ]
     vecinos = []

     for df ,dc in movimientos:
          nueva_fila = fila + df
          nueva_columna = columna + dc

          if (0<nueva_fila < filas -1 and 0 < nueva_columna < columnas -1):
               vecinos.append((nueva_fila, nueva_columna)) 
               return vecinos

def abir_camino(laberinto):
     laberinto[1][1]=0
     laberinto[1][2]=0
     laberinto[1][3]=0

     laberinto[2][3]=0

     laberinto[3][1]=0
     laberinto[3][2]=0
     laberinto[3][3]=0

def crear_laberinto(filas, columnas):
    

    laberinto = []

    for i in range(filas):
         # Creamos la matriz llena de paredes (1)
         
         fila = []

         for j in range(columnas):
              fila.append(1)

         laberinto.append(fila)
         # 2. Verificar que la matriz tenga tamaño antes de modificarla
    if filas < 3 or columnas < 3:
        raise ValueError("Las dimensiones deben ser al menos de 3x3")

         # Elegimos un punto de inicio, por ejemplo (1,1). y lo abrimos (0)
    inicio_fila, inicio_col =1,1
    laberinto[inicio_fila][inicio_col]=0

         # Inicializamos la pila con la posicion inicial

    pila = [(inicio_fila, inicio_col)]

         # Ciclo Principal del algoritmo de generacion

    while len(pila) > 0: 
              fila_actual, col_actual = pila[-1]

              #Usamos la funcion para obtener los vecinos a distancia 2
              vecinos = obtener_vecinos(fila_actual,col_actual,filas,columnas)

              #Filtramos solo los vecinos que sigan siendo paredes (no visitados)
              vecinos_no_visitados = []
              for f, c in vecinos: 
                   if laberinto[f][c]==1:
                        vecinos_no_visitados.append((f,c))  

              if vecinos_no_visitados:
              #Elegimos uno al azar de los vecinos
                sig_fila, sig_col = random.choice(vecinos_no_visitados)

              #Abrimos la pared intermedia entre la actual y la siguiente
                pared_fila = (fila_actual + sig_fila)//2
                pared_col= (col_actual + sig_col)//2

                laberinto[pared_fila][pared_col]=0
                laberinto[sig_fila][sig_col]=0

                #Agregamos la nueva celda a la pila
                pila.append((sig_fila,sig_col))
              else:
              #Si no hay salidas, hacemos backtracking (sacamos a la pila)
                pila.pop()
              


    return laberinto

