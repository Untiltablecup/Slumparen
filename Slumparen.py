import random

loop = (1)

while loop == (1):
    val = input("Vill du ha ett slumpat namn och efternamn eller slumpade kläder? \n>[Namn] eller [Kläder]\n>>>")
    
    if val.lower() == ("namn"):
        fornamn = ["Isak", "John", "Elsa", "Moa", "Kalle"]

        efternamn = ["Johansson", "Eriksson", "Karlsson", "Svensson", "Strömberg"]

        for i in range(0, 5):
            fornamnval = random.randint(0, len(fornamn)-1)
            efternamnval = random.randint(0, len(efternamn)-1)

        print (f"Namnet blev {fornamn[fornamnval]} {efternamn[efternamnval]}")
        loop = (0)    

    elif val.lower() == ("kläder"):
        overkropp = ["T-shirt", "luvtröja", "långärmad tröja", "skjorta"]

        underkropp = ["jeans", "cargobyxor", "shorts", "mjukisbyxor"]

        for i in range(0, 4):
            overkroppval = random.randint(0, len(overkropp)-1)
            underkroppval = random.randint(0, len(underkropp)-1)
        print (f"Du borde ha på dig en {overkropp[overkroppval]} och {underkropp[underkroppval]}")
        loop = 0

    else:
        print ("Snälla välj ett av de två valen som ges")
        continue