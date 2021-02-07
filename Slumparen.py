import random

Fornamn = ["Isak", "John", "Elsa", "Moa", "Kalle"]

Efternamn = ["Johansson", "Eriksson", "Karlsson", "Svensson", "Strömberg"]

for i in range(0, 5):
    Fornamnval = random.randint(0, len(Fornamn)-1)
    Efternamnval = random.randint(0, len(Efternamn)-1)

print (f"Din vänn heter {Fornamn[Fornamnval]} {Efternamn[Efternamnval]}")