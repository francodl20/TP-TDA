'''
Segunda parte: Mateo empieza a Jugar
Pasan los años. Mateo ahora tiene 7 años. Los mismos años que tenía Sophia cuando comenzaron
a jugar al juego de las monedas. Eso quiere decir que Mateo también ya aprendió sobre
algoritmos greedy, y lo comenzó a aplicar. Esto hace que ahora quién gane dependa más de
quién comience y un tanto de suerte.

Esto no le gusta nada a Sophia. Ella quiere estar segura de ganar siempre. Lo bueno es que ella
comenzó a aprender sobre programación dinámica. Ahora va a aplicar esta nueva técnica para
asegurarse ganar siempre que pueda.

Consigna
-Hacer un análisis del problema, plantear la ecuación de recurrencia correspondiente y proponer
un algoritmo por programación dinámica que obtenga la solución óptima al problema planteado: 
Dada la secuencia de monedas m1,m2,⋯,mn , sabiendo que Sophia empieza el juego y que Mateo 
siempre elegirá la moneda más grande para sí entre la primera y la última moneda en sus respectivos
turnos, definir qué monedas debe elegir Sophia para asegurarse obtener el máximo valor acumulado
posible. Esto no necesariamente le asegurará a Sophia ganar, ya que puede ser que esto no sea
obtenible, dado por cómo juega Mateo. Por ejemplo, para [1, 10, 5], no importa lo que haga Sophia,
Mateo ganará.

-Demostrar que la ecuación de recurrencia planteada en el punto anterior en efecto nos lleva a
obtener el máximo valor acumulado posible.

-Escribir el algoritmo planteado. 

-Describir y justificar la complejidad de dicho algoritmo. Analizar si (y cómo) afecta a los tiempos
del algoritmo planteado la variabilidad de los valores de las monedas.

-Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente,
el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también.

-Hacer mediciones de tiempos para corroborar la complejidad teórica indicada. Agregar los casos de prueba
necesarios para dicha corroboración (generando sus propios sets de datos). Esta corroboración empírica
debe realizarse confeccionando gráficos correspondientes, y utilizando la técnica de cuadrados mínimos.
Para esto, proveemos una explicación detallada, en conjunto de ejemplos.
Agregar cualquier conclusión que parezca relevante.

'''


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

def elegirMonedaConDinamica(sofia, coins):

    if(len(coins) < 4):
        return elegirMonedaConGreedy(sofia,coins)
    
    first = coins[0]
    second = coins[1]
    penultimate = coins[-2]
    last = coins[-1]


    first_case = first + (max(last,second)*(-1))
    second_case = last + (max(first,penultimate)*(-1)) 

    if(first_case >= second_case):
        sofia.append(first)
        coins.remove(first)
    else:
        sofia.append(last)
        coins.remove(last)
    
    return sofia, coins
    
def elegirMonedaConGreedy(mateo, coins):

    first = coins[0]
    last = coins[-1]

    best = max(first, last)

    mateo.append(best)
    coins.remove(best)

    return mateo,coins


def juegoMonedas(coins):
    #Turn positive=sofia negative=mateo

    #Empieza mateo
    turn = -1                        
    sofia = []
    mateo = []

    while coins:
        if turn > 0:
            sofia, coins = elegirMonedaConDinamica(sofia, coins)
            
        else:
            mateo, coins = elegirMonedaConGreedy(mateo, coins)

        turn *= -1

    return sofia,mateo


num = 1

while num != 0:
    num = input("Numero de ejemplo: ")
    file = num + ".txt"

    coins = readTxt(file)
    player1,player2 = juegoMonedas(coins)

    printResults(player1,player2)

    print("\n")