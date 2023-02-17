#JoelMalondaBeltrán

import random

#Booleana i comptadors per a iniciar les diferents condicions amb el seu respectiu valor.
continuar = True
partides = 0
contadormaxintents = 0
contadorminintents = 1000000
guanyades = 0
intentsguanyades = 0

print("Anem a adivinar un número del 1 al 100")

while continuar:

    numminim = 1
    nummaxim = 100
    partides = partides + 1

    secret = random.randint(numminim, nummaxim)

    

    maxintents = int(input("Quants intents vols realitzar?: "))
    #Bucles que es realitzaran quan començe el joc. Aquests ens diràn els intents que portem per partida, el rang del número a endevinar i el resultat de si hem o no guanyat la partida.
    for intent in range(1, maxintents + 1):

        num = int(input("Dis-me un número: "))

        if num < secret:

            if num < numminim:
                print("Tas tonto? Per a que poses un número menor del que tens?")
            else:
                numminim = num + 1
            print("intent: ", intent, "El número es més alt.")
            print("El rang està entre", numminim, " i ", nummaxim)

        elif num > secret:

            if num > nummaxim:
                print("Tas tonto? Per a que poses un número major del que tens?")
            else:
                nummaxim = num - 1
            print("intent: ", intent, "El número es més baix. ")
            print("El rang està entre", numminim, " i ", nummaxim)

        else: # if num == secret:
            print("Has encertat! Felicitats! Has utilitzat", intent , "intents.")
            guanyades += 1
            intentsguanyades += intent
            
            if intent < contadorminintents:
                contadorminintents = intent
        
            if intent > contadormaxintents:
                contadormaxintents = intent

            break

    else:
        print("Has esgotat els intents. Has perdut el joc, el numero era el ", secret)
    #Booleana que ens mostra si volem tornar a jugar o pel contrari, finalitzar el joc. Si es posa una resposta inorrecta, ens demanarà tornar a posar la resposta fins que siga correcta.
    valida = True
   
    while valida:
        seguir = input("Vols tornar a jugar?: (S,N) ")
        if seguir == "S":
            valida = False

        elif seguir == "N":
            valida = False
        else:
            print("Necesite una resposta vàlida")

    if seguir == "N":
        continuar = False

#Resultats finals del joc, en els que ens dirà quantes partides em guanyat, la mitja dels intents per partida, el total de partides guanyades, premis, etc...
print("Has jugat un total de", partides, "partides.")
if guanyades == 0:
    print("No has guanyat ninguna partida")
else:
    mitja = intentsguanyades / guanyades
    print("La mitja dels intents de les partides guanyades es ",mitja)
    print("El número màxims d'intents realitzats ha segut", contadormaxintents, " i el número mínim ha segut", contadorminintents)
    print("El total de partides guanyades es", guanyades)
for premi in range (guanyades):
    print("PREMI ",end="")
    print("")
    
