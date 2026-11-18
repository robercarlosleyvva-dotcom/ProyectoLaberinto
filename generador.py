import random
#Importa la libreria 'random' que se utiliza en el algoritmo para elegir aleatoriamente los pasillos


#Crear_laberinto: Crea la cuadricula completa de tamaño (fila x columnas)
#Rellenando TODAS las celdas con el numero "1" (Que en consola visualizamos como muros solidos ██ )
def crear_laberinto(filas, columnas):
    # Inicializar toda la matriz con paredes (1)
    laberinto = [[1 for _ in range(columnas)] for _ in range(filas)]
    
    # Empezar el backtracking en (1, 1)
    pila = [(1, 1)] #Crea una lista que actua como memoria de las celdas que vamos visitando
    laberinto[1][1] = 0  # Marcar inicio como pasillo libre


    #El ciclo se mantiene activo mientras haya coordenadas dentro de la pila. 
    #Toma la celda actual(f_act,c_act) mirando el utlimo elemento agregado (pila[-1]) sin sacarlo todavia.
    while len(pila) > 0:
        f_act, c_act = pila[-1]
        
        # Buscar vecinos a 2 celdas de distancia que sean paredes
        vecinos = []
        movimientos = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        
        for df, dc in movimientos:
          #Cambia la posicion 
            nf = f_act + df
            nc = c_act + dc 
            if 0 < nf < filas - 1 and 0 < nc < columnas - 1:
               #Verifica que la nueva posicion(nf, nc) este dentro de los limites del laberinto
                if laberinto[nf][nc] == 1:
                    vecinos.append((nf, nc, df, dc))
                    
        if vecinos:
            # Elegir un vecino aleatorio
            nf, nc, df, dc = random.choice(vecinos) #  Si encontro un vecino disponible elije uno al azar usando random.choice
            
            # Romper la pared del medio diviendo el desplazamiento entre 2  y la convierte en 0
            laberinto[f_act + df // 2][c_act + dc // 2] = 0
            
            # Marcar el nuevo vecino convertido en 0 como pasillo y lo agrega a la pila para avanzar hacia alla 
            laberinto[nf][nc] = 0
            pila.append((nf, nc))
        else:
            # Si la celda actual no tiene vecinos libres a su alrededor(callejon sin salida), ejecuta
            #pila.pop() para eliminarla de la memoria y retroceder a la celda anterior, buscando nuevas rutas que hayan quedado pendientes
            pila.pop()

   
    from collections import deque
    #Importa la estructura de datos deque(Cola eficiente)

     #Ubica las coordenadas de la meta (fin_f, fin_c) en la esquina inferior derecha
    fin_f = filas - 2,
    fin_c =columnas - 2

     #Esto fuerza a que la celda de la meta como sus vecinas superior e izquierda se conviertan en pasillos (0)
     #Asegurando que nunca queden atrapadas por un muro
     
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
