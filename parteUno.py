'''

Primera parte: Introducción y primeros años
Cuando Mateo nació, Sophia estaba muy contenta. Finalmente tendría un hermano con quien 
    jugar. Sophi tenía 3 años cuando Mateo nació. Ya desde muy chicos, ella jugaba mucho 
    con su hermano.

Pasaron los años, y fueron cambiando los juegos. Cuando Mateo cumplió 4 años, el padre de 
    ambos le explicó un juego a Sophia: Se dispone una fila de n monedas, de diferentes 
    valores. En cada turno, un jugador debe elegir alguna moneda. Pero no puede elegir 
    cualquiera: sólo puede elegir o bien la primera de la fila, o bien la última. Al 
    elegirla, la remueve de la fila, y le toca luego al otro jugador, quien debe elegir 
    otra moneda siguiendo la misma regla. Siguen agarrando monedas hasta que no quede 
    ninguna. Quien gane será quien tenga el mayor valor acumulado (por sumatoria).

El problema es que Mateo es aún pequeño para entender cómo funciona esto, por lo que 
    Sophia debe elegir las monedas por él. Digamos, Mateo está “jugando”. Aquí surge otro 
    problema: Sophia es muy competitiva. Será buena hermana, pero no se va a dejar ganar 
    (consideremos que tiene 7 nada más). Todo lo contrario. En la primaria aprendió algunas 
    cosas sobre algoritmos greedy, y lo va a aplicar.

Consigna
-Hacer un análisis del problema, y proponer un algoritmo greedy que obtenga la solución 
    óptima al problema planteado: Dados los n valores de todas las monedas, indicar qué 
    monedas debe ir eligiendo Sophia para si misma y para Mateo, de tal forma que se 
    asegure de ganar siempre. Considerar que Sophia siempre comienza (para sí misma).
-Demostrar que el algoritmo planteado obtiene siempre la solución óptima (desestimando 
    el caso de una cantidad par de monedas de mismo valor, en cuyo caso siempre sería 
    empate más allá de la estrategia de Sophia).
-Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. 
    Analizar si (y cómo) afecta la variabilidad de los valores de las diferentes monedas a 
    los tiempos del algoritmo planteado.
-Analizar si (y cómo) afecta la variabilidad de los valores de las diferentes monedas a la 
    optimalidad del algoritmo planteado.
-Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. 
    Adicionalmente, el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también.
-Hacer mediciones de tiempos para corroborar la complejidad teórica indicada. Agregar los 
    casos de prueba necesarios para dicha corroboración. Esta corroboración empírica debe realizarse confeccionando gráficos correspondientes, y utilizando la técnica de cuadrados mínimos. Para esto, proveemos una explicación detallada, en conjunto de ejemplos.
-Agregar cualquier conclusión que les parezca relevante.

'''

#   Fila de monedas, se agarra primera o última
#   Sofia agarra el mayor valor disponible el hermano agarra el menor
#   Algoritmo greedy

def readTxt(txt):
    
    #Input coins txt
    coins = open(txt)
    #Skip first line
    coins.readline()
    #Build array of coin values
    coinsArray = []
    tempNum = ""

    for i in coins.read():
        if i != ";":
            tempNum += i
        else:
            coinsArray.append(int(tempNum))
            tempNum = ""
    coinsArray.append(int(tempNum))

    return coinsArray

def sumArray(array):
    result = 0
    for i in array:
        result += i
    return result

def printResults(sofia, mateo):

    print("Sofia: ")
    #print(sofia)
    valueSofia = sumArray(sofia)
    print(valueSofia)
    print("Cantidad: " + str(len(sofia)))
    print("Mateo: ")
    #print(mateo)
    valueMateo = sumArray(mateo)
    print(valueMateo)
    print("Cantidad: " + str(len(mateo)))

    if valueSofia > valueMateo:
        print("Gano Sofia !!!!!!!!!!!!!")
    elif valueSofia < valueMateo:
        print("Gano Mateo !!!!!!!!!!!!!")
    else:
        print("Empate ????")

def sofiaGreedy(coins):
    #Turn positive=sofia negative=mateo
    turn = 1
    sofia = []
    mateo = []

    while coins:
        if turn > 0:
            first = coins[0]
            last = coins[-1]
            best = max(first, last)

            sofia.append(best)
            coins.remove(best)
        else:
            first = coins[0]
            last = coins[-1]
            worst = min(first, last)

            mateo.append(worst)
            coins.remove(worst)
        turn *= -1

    printResults(sofia, mateo)
    


num = 1

while num != 0:
    num = input("Numero de ejemplo: ")
    file = num + ".txt"

    coins = readTxt(file)
    sofiaGreedy(coins)

    print("\n")