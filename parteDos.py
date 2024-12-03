'''
Segunda parte: Mateo empieza a Jugar
Pasan los años. Mateo ahora tiene 7 años. Los mismos años que tenía Sophia cuando comenzaron 
    a jugar al juego de las monedas. Eso quiere decir que Mateo también ya aprendió sobre 
    algoritmos greedy, y lo comenzó a aplicar. Esto hace que ahora quién gane dependa más 
    de quién comience y un tanto de suerte.

Esto no le gusta nada a Sophia. Ella quiere estar segura de ganar siempre. Lo bueno es que 
    ella comenzó a aprender sobre programación dinámica. Ahora va a aplicar esta nueva 
    técnica para asegurarse ganar siempre que pueda.

Consigna
-Hacer un análisis del problema, plantear la ecuación de recurrencia correspondiente y 
    proponer un algoritmo por programación dinámica que obtenga la solución óptima al 
    problema planteado: Dada la secuencia de monedas m1,m2,⋯,mn, sabiendo que Sophia 
    empieza el juego y que Mateo siempre elegirá la moneda más grande para sí entre la 
    primera y la última moneda en sus respectivos turnos, definir qué monedas debe elegir 
    Sophia para asegurarse obtener el máximo valor acumulado posible. Esto no necesariamente 
    le asegurará a Sophia ganar, ya que puede ser que esto no sea obtenible, dado por cómo 
    juega Mateo. Por ejemplo, para [1, 10, 5], no importa lo que haga Sophia, Mateo ganará.
-Demostrar que la ecuación de recurrencia planteada en el punto anterior en efecto nos lleva 
    a obtener el máximo valor acumulado posible.
-Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. 
    Analizar si (y cómo) afecta a los tiempos del algoritmo planteado la variabilidad de 
    los valores de las monedas.
-Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. 
    Adicionalmente, el curso proveerá con algunos casos particulares que deben cumplirse 
    su optimalidad también.
-Hacer mediciones de tiempos para corroborar la complejidad teórica indicada. 
    Agregar los casos de prueba necesarios para dicha corroboración (generando sus propios 
    sets de datos). Esta corroboración empírica debe realizarse confeccionando gráficos 
    correspondientes, y utilizando la técnica de cuadrados mínimos. Para esto, proveemos 
    una explicación detallada, en conjunto de ejemplos.
-Agregar cualquier conclusión que parezca relevante

'''

#   Fila de monedas, se agarra primera o última
#   Sofia usa "nueva tecnica" y mateo elige el mayor valor disponible
#   Algoritmo de programacion dinamica

import time

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

def sofiaRecursive(coins, firstI, lastI, memo):

    first = coins[firstI]
    last = coins[lastI]

    notes = []

    if (firstI - lastI) >= 0:
        return notes, 0

    if memo[0][firstI][lastI] != -1:
        return memo[1][firstI][lastI], memo[0][firstI][lastI]

    if (firstI - lastI) == -1:
        best = max(first, last)
        notes.append(best)

        memo[0][firstI][lastI] = best
        memo[1][firstI][lastI] = notes

        return notes, best
    elif (firstI - lastI) == -2:
        if first >= last:
            minimum = min(coins[firstI + 1], last)
            notes.append(minimum)
            notes.append(first)

            maxSum = first + minimum
            memo[0][firstI][lastI] = maxSum
            memo[1][firstI][lastI] = notes

            return notes, maxSum
        else:
            minimum = min(first, coins[firstI + 1])
            notes.append(minimum)
            notes.append(last)

            maxSum = last + minimum
            memo[0][firstI][lastI] = maxSum
            memo[1][firstI][lastI] = notes

            return notes, maxSum

    second = coins[firstI + 1]
    secondLast = coins[lastI - 1]

    #If choosing first
    if second >= last:
        notes1, firstPath = sofiaRecursive(coins, firstI + 2, lastI, memo)
        firstPath += first
    else:
        notes1, firstPath = sofiaRecursive(coins, firstI + 1, lastI - 1, memo)
        firstPath += first

    #If choosing second
    if first >= secondLast:
        notes2, lastPath = sofiaRecursive(coins, firstI + 1, lastI - 1, memo)
        lastPath += last
    else:
        notes2, lastPath = sofiaRecursive(coins, firstI, lastI - 2, memo)
        lastPath += last

    if firstPath >= lastPath:
        notes = notes1
        notes.append(first)
        maxSum = firstPath
    else:
        notes = notes2
        notes.append(last)
        maxSum = lastPath

    memo[0][firstI][lastI] = maxSum
    memo[1][firstI][lastI] = notes

    return notes, maxSum

def sofiaSelection(notes):
    return notes.pop(0)

def mateoSelection(coins):
    first = coins[0]
    last = coins[-1]
    best = max(first, last)

    return best

def sofiaPD(coins):
    #Turn positive=sofia negative=mateo
    turn = 1
    sofia = []
    mateo = []
    notes = []
    memo = [[[-1 if a==0 else [] for _ in range(len(coins))] for _ in range(len(coins))] for a in range(2)]

    notes, result = sofiaRecursive(coins, 0, len(coins) - 1, memo)

    notes.reverse()

    while coins:
        if turn > 0:
            best = sofiaSelection(notes)

            sofia.append(best)
            coins.remove(best)
        else:
            worst = mateoSelection(coins)

            mateo.append(worst)
            coins.remove(worst)
        turn *= -1

    printResults(sofia, mateo)

num = 1

while num != 0:
    num = input("Numero de ejemplo: ")
    file = num + ".txt"

    start = time.time()
    coins = readTxt(file)
    sofiaPD(coins)
    end = time.time()
    
    print("Tiempo: ", end - start)

    print("\n")