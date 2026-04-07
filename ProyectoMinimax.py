import random
import math

ancho = random.randint(5, 8)
alto = random.randint(5, 8)

while True:
    posicion_R = (random.randint(1, alto-2), random.randint(1, ancho-2))
    posicion_G = (random.randint(1, alto-2), random.randint(1, ancho-2))
    if posicion_R != posicion_G:
        break

def crear_tablero(pos_R, pos_G):
    tablero = []
    for r in range(alto):
        fila = []
        for c in range(ancho):
            if r == 0 or r == alto-1 or c == 0 or c == ancho-1:
                fila.append("*")
            elif (r,c) == pos_G:
                fila.append("G")
            elif (r,c) == pos_R:
                fila.append("R")
            else:
                fila.append(" ")
        tablero.append(fila)
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

def distanciaMH(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def movimientos_validos(pos, es_gato=False):
    x, y = pos
    if es_gato:
        posibles = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    else:
        posibles = [
            (x-1,y-1),(x-1,y),(x-1,y+1),
            (x,y-1),         (x,y+1),
            (x+1,y-1),(x+1,y),(x+1,y+1)
        ]
    return [(nx,ny) for nx,ny in posibles if 1<=nx<alto-1 and 1<=ny<ancho-1]

def evaluar(pos_R, pos_G):
    return distanciaMH(pos_R, pos_G)

def minimax(pos_R, pos_G, profundidad, es_turno_R):
    if pos_R == pos_G or profundidad == 0:
        return evaluar(pos_R, pos_G), None

    if es_turno_R:
        mejor_val = -math.inf
        mejor_mov = pos_R
        for mov in movimientos_validos(pos_R, es_gato=False):
            val, _ = minimax(mov, pos_G, profundidad-1, False)
            if val > mejor_val or (val == mejor_val and distanciaMH(mov, pos_G) > distanciaMH(mejor_mov, pos_G)):
                mejor_val = val
                mejor_mov = mov
        return mejor_val, mejor_mov
    else:
        mejor_val = math.inf
        mejor_mov = pos_G
        for mov in movimientos_validos(pos_G, es_gato=True):
            val, _ = minimax(pos_R, mov, profundidad-1, True)
            if val < mejor_val or (val == mejor_val and distanciaMH(pos_R, mov) < distanciaMH(pos_R, mejor_mov)):
                mejor_val = val
                mejor_mov = mov
        return mejor_val, mejor_mov

turno = 0
turnos_escape = 0
prof_inicial = 1
prof_max = 3

print("Posición inicial:")
mostrar_tablero(crear_tablero(posicion_R, posicion_G))

while posicion_R != posicion_G:
    prof_G = prof_inicial if turno < 2 else prof_max
    prof_R = prof_inicial if turno < 2 else prof_max
    
    _, nueva_pos_G = minimax(posicion_R, posicion_G, prof_G, False)
    posicion_G = nueva_pos_G
    print(f"Turno {turno} - Gato se mueve:")
    mostrar_tablero(crear_tablero(posicion_R, posicion_G))
    
    if posicion_R == posicion_G:
        print(f"El Gato atrapó al Ratón en {turno} turnos. ¡Victoria del Gato!")
        break
    
    _, nueva_pos_R = minimax(posicion_R, posicion_G, prof_R, True)
    posicion_R = nueva_pos_R
    print(f"Turno {turno} - Ratón se mueve:")
    mostrar_tablero(crear_tablero(posicion_R, posicion_G))

    turnos_escape += 1
    turno += 1
    
    if turnos_escape >= 4:
        print("El Ratón logró sobrevivir 4 movimientos. ¡Victoria del Ratón!")
        break