#importamos nuestras dependencias
import random
import math

#asignamos al tablero valores randoms , con la funcion randinti y le pasamos los parametros nuestros parametos serian desde 5 hata 8
ancho = random.randint(5, 8)
alto = random.randint(5, 8)

# Ponemos a nuestros personajes en el mapa , los pongo en su posicion inicial de forma aleatoria 
#estariamos haciendo lo mismo que con los valores de ancho y alto , pero esto valores son tuplas  uso tuplas porque 
#Las tuplas son ideales para representar datos que lógicamente van juntos y cuya estructura no va a variar:

#Coordenadas geográficas: (latitud, longitud)
#en este caso lo uso para ir cambiado el valor de las variables de la tupla y asi poder mover mis personajes 
while True:
    posicion_R = (random.randint(1, alto-2), random.randint(1, ancho-2))
    posicion_G = (random.randint(1, alto-2), random.randint(1, ancho-2))
    if posicion_R != posicion_G:
        break

# Creo un tablero con dos for anidados y una lista 
def crear_tablero(pos_R, pos_G):# le paso al tablero la posicion del Gato y del raton para poder usarlos dentro de la funcion le pasamos los argumentos de sus posiciones 
    tablero = []# declaro una lista vacia porque la vamos a llenar con los muros y espacios del tablero q vamos a crear alto y ancho son nuestros parametros 
    #alto representa la cantidad de filas y ancho la cantidad de columnas
    #en si creo mi matris llenando la varias veces de lista y la recorro sus posiciones con el ford anidado 

    for r in range(alto):
        fila = []
        for c in range(ancho):
            if r == 0 or r == alto-1 or c == 0 or c == ancho-1:# en esta condicion prefunto si si las posiciones estan en los bordes para agregar dentro de mi lista este
                #simbolo q representa mis muros  *
                fila.append("*")
            elif (r,c) == pos_G:# aca agrupo a r y c en una tupla y le preguno si son iguales a los valores de Pos_G y Pos_R no hay q olvidar q estos dos varables contienen tuplas dentro 
                fila.append("G")# si la condicion se cumple agregamos a la lista , el valor de G o R dependiendo de la posicion
            elif (r,c) == pos_R:# hacemos lo mismo con valor de Raton 
                fila.append("R")
            else:# si ninguna de las condiciones anteriores funciona  sera igual a espacio vacio 
                fila.append(" ")
        tablero.append(fila)#agregamos la lista dentro de la matriz tablero 
    return tablero

# para esta funcion simplemente mostramos el tablero lo imprimimos lo recorremos de esta manera como tablero es una lista de lista lo unico q hacemos
#es q en el for  le pasamos for fila q seria la lista completa  in tablero q guarda las lista completas y se iprimiria la primera fila (lista completa) en cada iteracion 
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

# es una formula matematica por la cual podemos saber la distancia entre dos objetos , la formula es restamos
# restamos la posicion de de los dos objetos  (x,y) y el resultado los sumamos  (x1-x2)+(y1-y2) siempre nos tendria q dar un resultado positivo 
#por eso uso abs en los dos parentesis para convertir cada numero en un valor absoluto positivo asi nunca nos sale negativo  
# abs q signifaca valor apsoluto es como un filtro q elimina el signo negativo de cualquier numero 
def distanciaMH(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# en la funcion de movimientos validos lo q hacemos en ver si el raton y el gato no chocan por la pared
#si no chocan sus movimiento son validos ya q sus movimientos son tuplas entran dentro de una lista de tuplas

def movimientos_validos(pos, es_gato=False):
    x,y = pos#Aca como pos es una tupla estamos desempaquetando sus valores y repartiendolos en x , y 
    if es_gato:
        posibles = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]# usamos la posicion actual la sumamos y restamos y tenemos las posiciones futuras 
        #q puede hacer en un turno recordar q solo podemos ir de una casilla por turno por eso +1 y-1
        
    else:#lo mismo hacemos con las posiciones del raton pero ya q el es mas agil puede moverse en 8 direcciones
        
        posibles = [
            (x-1,y-1),(x-1,y),(x-1,y+1),
            (x,y-1),        (x,y+1),
            (x+1,y-1),(x+1,y),(x+1,y+1)
        ]
    #esta linea de aca puede parecer confusa pero es muy simple parece un operador ternario pero no lo es
    #es un List Comprehension (Comprensión de Listas) con un filtro condicional 
    #es una forma corta de hacer esto en una sola linea # Esto es lo que pasa "por dentro" de esa línea:
#lista_final = []
#for nx, ny in posibles:
#   if 1 <= nx < alto-1 and 1 <= ny < ancho-1:
#       lista_final.append((nx, ny))
#return lista_final
#porque lo uso en codigo profesinal lei q lo usan mucho y es muy genial de usar me gusta usarlo y me hace aprender a
#optimizar mi codigo hacerlo menos largo y subir un nivel mas de aprendizaje 
#aca es donde retornamos una lista de tuplas con movimientos validos ,los movimientos validos son todos
#los q no toquen los muros (usamos obviamente sus posiciones para saber q no tocamos un muro)
    return [(nx,ny) for nx,ny in posibles if 1<=nx<alto-1 and 1<=ny<ancho-1]

# esta funcion solo la llama el caso base cuando la profundidad es 0 
# esta funcion se llama muchas veces en la recursividad , recibe los ultimas posiciones de la recursividad
# y lo q hace es ver si es posiciones las cuales la recursividad llego son las mejores osea no hace eso en esta funcion
#lo q hace es q en la recursividad al final cuando llega al caso base con las posiciones finales de esa recursividad las calcula
# con la distancia manhattan y si las posicones  y el valor son las mejores esta serian la mejor posicon y el mejor valor 
#eso se compara en el for , aca solo calculamos y retornamos y valor  y el for guarda las mejores posiciones si es q el valor es el mejor
#Por eso  esta funcion es la heurística porque estima qué tan cerca estás de ganar sin haber terminado el juego real
def evaluar(pos_R, pos_G):
    return distanciaMH(pos_R,pos_G)

# --- Minimax ---
def minimax(pos_R, pos_G, profundidad, es_turno_R):# aca usamos los argumentos q le pasamos a la funcion posiciones y profunidad y el buleano q le pasamos indica el turno de quien es
    #si es false es turno del Gato y si es verdadero es turno del raton 

    #Caso Base 
    #este if detiene la recursivdiad porque minimax se llama asi mismo varias veces y a otras funciones pero esta es para salir de la 
    #recursividad para de minimax se detiene si en alguno de los movimientos futuros raton pierde o la profundidad llega a cero 
    if pos_R == pos_G or profundidad == 0:
        return evaluar(pos_R,pos_G), None
    

    #turno del raton si es_turno_R  es verdadero 
    if es_turno_R:
        # Ratón maximiza
        mejor_val = -math.inf #declaramos q el mejor valor es igual a menos infinito porque , cualquier valor sgt va ser mayor y podra remplazarlos , mas porque necesitamos 
        #un valor q no cause conflicto ala hora de remplazarlo 

        mejor_mov = pos_R #declaramos q la mejor posicion es igual a la tupla de la posicion q esta en el argumento q le pasamos 

        # le decimos q vamos a recorrer todos los movimientos(mov ) q esteen dentro de la funcion  movimeintos_validos y le pasamos los argumentos q serian las posiciones del 
        # raton y el gato  y buleano como parametros para la funcion esta nos devolvera
        #una lista de tuplas q tienen movimientos validos 
        for mov in movimientos_validos(pos_R, es_gato=False):
            val, _ = minimax(mov, pos_G, profundidad-1, False)
            if val > mejor_val or (val == mejor_val and distanciaMH(mov,pos_G) > distanciaMH(mejor_mov,pos_G)):
                mejor_val = val
                mejor_mov = mov
        return mejor_val, mejor_mov
    
    #el primer movimiento siempre  comenzamos primero con el raton como la profundidad es 1 
    #y en el for nosotros ponemos profundidad-1 la profundidad queda como 0 y recorre las 4 movimeintos posibles 
    #solo 4 por q siempre q llama a minimax se topa con la primera condicion del caso base y retorna el mejor valor
    # y como es la primera vez no va ser un movimiento tonto por asi decilor porq nunca usa de referencia los movimeintos futuros del raton
    #despues ya cambia la cosa en el turno 2 la profundidad es 3-1 y cada vez q entra en el for q recorre otro valor 
    #el for del gato llamo al del movimiento del raton llamanod a mas funciones verdad(es largo de explicar)
    # y el raton hace lo mismo q el gato casi lo mismo porq el raton tiene 8 movimientos 
    #y para la recursividad sale de ese buclue cuando la profundidad llega a cero , para los dos para el gato y el raton 
    # ahi es donde actua nuestro caso base y para la recursividad
    else:
        # Gato minimiza
        mejor_val = math.inf
        mejor_mov = pos_G
        for mov in movimientos_validos(pos_G, es_gato=True):
            val, _ = minimax(pos_R, mov, profundidad-1, True)
            # 1. Comparamos si el nuevo valor proyectado al futuro (val) es mejor que el actual (mejor_val).
# 2. Si hay un empate en el futuro (val == mejor_val), desempatamos usando la 
#    distancia inmediata: elegimos el movimiento que acerque más al personaje 
#para eso comparamos la distancia q hay en el turno actual distancia(posicion del raton, mov movimiento actual) si este es menor a distanciaMH(posicion del raton, el mejor movimiento pasado)

# sino este seguira siendo el mejor valor y el mejor movmiento 
            if val < mejor_val or (val == mejor_val and distanciaMH(pos_R,mov) < distanciaMH(pos_R,mejor_mov)):
                mejor_val = val
                mejor_mov = mov
        return mejor_val, mejor_mov

# --- Simulación ---
turno = 0 # esta varable representa los turnos del Gato 
turnos_escape = 0#esta representa los turnos del Raton 
prof_inicial = 1# esta variable representa la profundidad q usaremos en el minimax , como el juego decia q el gato y el raton comenzarian con movimeintos 
#no tan inteligentes  y irian evolucionando , pense q la mejor manera de simular eso seria aumentando la profundidad en cada turno 
# la profundida es cuantas veces mira hacia el futuro o juega posiciones dentro del minimax 
prof_max = 3# esta es la profundidad maxima el limite 

# imprimimos la posicion inicial de los personajes en el juego con nuestras respectivas funciones 
print("Posición inicial:")# un mensajito para indicar q esta es la posicion inicial en la q comenzamos 
mostrar_tablero(crear_tablero(posicion_R,posicion_G))# llamamos a la funcion y le pasamos los argumentos de Posicion R y Posicion G q son tuplas 
# y son la primera posicion de gato y raton q son aleatorias
while posicion_R != posicion_G: # este siclo while le puse q el siclo va seguir repitendo MIENTRAS la posicon de Raton y Gato sean diferentes si son iguales significa q 
    #Gato atrapo a Raton y salen del bucle 
    #esto seria un operador ternario dentro de una variable 
    #es una forma elegante de hacer codigo largo en una sola liena 
    #la linea se lee de izquierda a derecha 
    # si turno es menor a 2 profundidad va ser igual a Profundidad Inicial 
    #sino profundidad va ser igual a profundidad maxima 

    prof_G = prof_inicial if turno < 2 else prof_max
    prof_R = prof_inicial if turno < 2 else prof_max
    
    # aca uso para declarar la variable uso un metodo de python  q se llama Desempaquetado de Iterables 
    #tambien uso el concepto de  Variable Dummy (variable de relleno) o Variable Desechable.
    #lo que hacemos es desarmar la tupla que devuelve la función y repartir sus valores en dos variables distintas en una sola línea 
    # porque la funcion minimax nos va devolver una tupla y nostros solo queremos un valor de ella y el dato basura por asi decirlo se va a la variable barra baja 
    # se separa asi  variable_basura,variable_a_utilizar  en mi caso _, nueva_pos_G
    _, nueva_pos_G = minimax(posicion_R,posicion_G,prof_G,False)#la variable es igual al valor q le va retornar minimax , asiq  le llamamos a la funcion y le pasamos 
    #los parametros de Posicion del raton ,Posicion del Gato y , profundidad de gato en este turno (no olvidar q sus profundiades aumentan en cada turno), y el valor false 
    posicion_G = nueva_pos_G # minimax devuelve la nueva posicion asi q decalramos q Posicion_G ahora va ser a nueva posicion de Gato 
    print(f"Turno {turno} - Gato se mueve:")#para q quede lindo imprimimos de quien es el turno tambien la cantidad de turnos
    mostrar_tablero(crear_tablero(posicion_R,posicion_G))#le pasamos a mostrar tablero las tuplas con sus nuevas posiciones y imprimimos 
    #casi me olvido mostrar tablero llama a crear tablero porque tenemos q crear de nuevo el tablero con las nuevas posiciones de los personajes
    #mostrar tablero llama a crear tablero le pasamos los argumentos se crea el tablero nuevo despues con esos valores nuevos se crea el tablero nuevo 
    
    #hacemos esta verificacion antes q raton se mueva para ver si gato gano asi es mas preciso el juego 
    # puse una condicion parecida al principio pero esta tiene q esperar a q todo lo q esta dentro del bucle pase para poder verificar 
    #al hacer verificar las posiciones justo despues de q gato se mueva es mas preciso cuando gato gana 
    if posicion_R == posicion_G:# como sabemos si gato gano su posicion va ser igual a la de raton 
        # NUEVA PARTE: Imprimimos el mensaje aquí porque el 'break' impide que el 'else' del while se ejecute.
        print(f"El Gato atrapó al Ratón en {turno} turnos. ¡Victoria del Gato!")
        break# paramos el bucle y entraria en el else del while imprimiendo q  la victoria es de gato 
    
    # --- Ratón ---
    #hacemos lo mismo q con Gato para raton le pasamos los mismos argumentos 
    _, nueva_pos_R = minimax(posicion_R,posicion_G,prof_R,True)

    posicion_R = nueva_pos_R
    print(f"Turno {turno} - Ratón se mueve:")
    # NUEVA PARTE: Mostramos el tablero después del movimiento del Ratón para ver cada paso.
    mostrar_tablero(crear_tablero(posicion_R, posicion_G))

    turnos_escape += 1#este es un contador q cuenta las veces q raton se mueve 
    
    turno += 1# esta variable de turno tambien es contadora , cada q suma esta hace mas grande la profundidad 
    
    if turnos_escape >= 4:# verificamos si raton sobrevivio 4 turnos si lo hace raton gana 
        print("El Ratón logró sobrevivir 4 movimientos. ¡Victoria del Ratón!")
        break