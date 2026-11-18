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

# generador.py


def crear_laberinto(filas, columnas):
    # Inicializar toda la matriz con paredes (1)
    laberinto = [[1 for _ in range(columnas)] for _ in range(filas)]
    
    # Empezar el backtracking en (1, 1)
    pila = [(1, 1)]
    laberinto[1][1] = 0  # Marcar inicio como pasillo
    
    while len(pila) > 0:
        f_act, c_act = pila[-1]
        
        # Buscar vecinos a 2 celdas de distancia que sean paredes
        vecinos = []
        movimientos = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        
        for df, dc in movimientos:
            nf, nc = f_act + df, c_act + dc
            if 0 < nf < filas - 1 and 0 < nc < columnas - 1:
                if laberinto[nf][nc] == 1:
                    vecinos.append((nf, nc, df, dc))
                    
        if vecinos:
            # Elegir un vecino aleatorio
            nf, nc, df, dc = random.choice(vecinos)
            
            # Romper la pared intermedia (la que está a la mitad)
            laberinto[f_act + df // 2][c_act + dc // 2] = 0
            
            # Marcar el nuevo vecino como pasillo y meterlo a la pila
            laberinto[nf][nc] = 0
            pila.append((nf, nc))
        else:
            # Si no hay vecinos libres, retroceder (backtrack)
            pila.pop()

    # === GARANTIZAR SALIDAS LIBRES PARA INICIO Y FIN ===
   # === GARANTIZAR CONECTIVIDAD TOTAL ENTRE INICIO Y FIN ===
   # === GARANTIZAR CONECTIVIDAD ABSOLUTA EN LA META ===
    from collections import deque

    fin_f, fin_c = filas - 2, columnas - 2
    laberinto[fin_f][fin_c] = 0        # La E es transitable
    laberinto[fin_f - 1][fin_c] = 0    # Forzar celda superior abierta
    laberinto[fin_f][fin_c - 1] = 0    # Forzar celda izquierda abierta
    
    # Verificación rápida con BFS para comprobar si hay ruta del (1,1) al (fin_f, fin_c)
    cola = deque([(1, 1)])
    visitados = {(1, 1)}
    encontrado = False

    while cola:
        f, c = cola.popleft()
        if (f, c) == (fin_f, fin_c):
            encontrado = True
            break
        for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nf, nc = f + df, c + dc
            if 0 <= nf < filas and 0 <= nc < columnas:
                if laberinto[nf][nc] == 0 and (nf, nc) not in visitados:
                    visitados.add((nf, nc))
                    cola.append((nf, nc))

    # Si por alguna razón extrema sigue desconectado, carveamos un pasillo seguro en "L"
    if not encontrado:
        f, c = fin_f, fin_c
        while f > 1:
            laberinto[f][c] = 0
            f -= 1
        while c > 1:
            laberinto[f][c] = 0
            c -= 1

    return laberinto
