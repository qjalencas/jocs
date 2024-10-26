import random

def secretPanel(p):
    result = ""
    for i in p:
        if i == " ":
            result += i
        else:
            result += "-"
    return result


def updateSecretWord(w, sw, c):
    swupdated = ""
    for i in range(0, len(w)):
        if c == w[i]:
            swupdated += w[i]
        else:
            swupdated += sw[i]
    return swupdated


def updatePoints(sw, c):
    count = 0
    for i in sw:
        if i == c:
            count += 1
    return count


def correctPanel(w, sol):
    for i in range(0, len(w)):
        if w[i] != sol[i]:
            return False
    return True

def choosePanel():
    
    frases = [
        "El sol brilla sobre la ciutat cada mati",
        "Un dia de pluja es perfecte per llegir",
        "Els gats son animals molt misteriosos",
        "La musica ens acompanya en moments durs",
        "La natura ens ofereix belleses infinides",
        "Una bona tassa de te sempre alegra",
        "Les estrelles brillen amb força a la nit",
        "El mar tranquil transmet una gran pau",
        "Les flors decoren els nostres jardins encantats",
        "Un bon llibre es un viatge sense final",
        "Les amistats veritables son un tresor",
        "Els somnis son la clau del nostre futur",
        "Un viatge llarg es recorda per sempre",
        "La cuina es un art que ens uneix a tots",
    ]
    
    return random.choice(frases)


def roulette():
    caselles = []
    caselles += ["10€"] * 10
    caselles += ["50€"] * 5
    caselles += ["100€"] * 2
    caselles += ["DUPLICAR"] * 2
    caselles += ["BANCARROTA"] * 2
    return random.choice(caselles)

def startGame():
    
    # Variable del saldo
    saldo = 0
    
    # Triar la frase
    w = choosePanel().upper()
    
    # Mostrar la frase oculta
    sw = secretPanel(w)
    print(sw)
    while True:
        # Escollir accio
        accio = None
        accio = input("Que fas: resols el panell[P] o tires de la ruleta[R]?")
        accio = accio.upper()
        while accio not in "RP":
            print("No pots fer això")
            accio = input("Que fas: resols el panell[P] o tires de la ruleta[R]?")
            accio = accio.upper()




        if accio == "P":
            sol = input("Posa la frase: ").upper()
            if w == sol:
                print("Enhorabona! Has guanyat %d €" % saldo)
                return saldo
            else:
                print("Mala sort! La frase era '%s'. No t'emportes res!" % w)
                return 0

        elif accio == "R":
            # Tirar la ruleta
            result = roulette()
            print("Ha tocat " + result)

            if result in ["10€", "50€", "100€"]:
                c = input("Digues una lletra")
                c = c.upper()
                sw = updateSecretWord(w, sw, c)
                print()
                print(sw)
                print()
                count = updatePoints(sw, c)
                guanyes = int(result[:-1]) * count
                print("N'hi ha %d. Has guanyat %d €" % (count, guanyes))
                saldo += guanyes

            elif result == "DUPLICAR":
                saldo = saldo * 2

            elif result == "BANCARROTA":
                saldo = 0

            print("Tens %d € " % saldo)
            print()
           
    
startGame()