import heapq #Cola de prioridad

def dijkstra(laberinto, inicio, fin):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    #pq almacena : (costo_acomulado, fila, columna)
    #pq significa Priority Queue  = Cola de Prioridad
    pq = [(0, inicio[0], inicio[1])]

    #Diccionarios para controlar costos minimos y reconstruir la ruta
    costos = {inicio:0}
    padres = {inicio: None}

    nodos_explorados = 0

    #Movimientos posibles para recorrer los pasillos (4 direcciones)
    movimientos = [(-1,0),(1,0),(0,-1),(0,1)]

    while pq:
        costo_actual, f_act, c_act = heapq.heappop(pq)
        nodos_explorados +=1

        #Si llegamos al destino, detenemos la busqueda
        if (f_act, c_act)== fin:
            break

        #Si ya encontramos un camino mejor a esta celda, ignoramos
            #(f_act, c_act) construye una tupla
        if costo_actual > costos.get((f_act, c_act), float('inf')):
                            #Busca la clave, si existe devuelve el elemento en esa posicion
                                #Si no existe : devuelve infinito
            continue

        #Va recorriendo la lista:    
        for df, dc in movimientos:
            nf, nc = f_act + df, c_act + dc


            #Validar que esté dentro de los límites y no sea pared (1)
            if 0 <= nf < filas  and 0 <= nc < columnas:
                if laberinto[nf][nc]!=1 :
                    #Costo de paso por celda(por ahora 1)
                    peso_celda=1
                    nuevo_costo = costo_actual + peso_celda

                    vecino = (nf,nc)
                    if nuevo_costo < costos.get(vecino, float('inf')):
                        costos[vecino] = nuevo_costo
                        padres[vecino]= (f_act,c_act)
                        heapq.heappush(pq, (nuevo_costo,nf,nc))

    #Reconstruir la ruta desde el fin hasta el inicio
    ruta =[]
    actual = fin

    if actual in padres or actual== inicio:
        while actual is not None:
            ruta.append(actual)
            actual= padres.get(actual)
        ruta.reverse()#Invertir para que vaya de Inicio -> Fin

    costo_total = costos.get(fin,float('inf'))

    return ruta, costo_total,nodos_explorados

