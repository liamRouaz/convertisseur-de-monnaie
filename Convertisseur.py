franc = 6.55957
dollar = 1.42408
livre = 0.795447
livres = 0
francs = 0
dollars = 0

print("Bonjour, que voulez-vous faire?")
print("1-Conversions euros/francs", "\n2-Conversions euros/dollars", "\n3-Conversions euros/livres")

choix = int(input())  # Utilisez int() pour convertir l'entrée en entier

if choix == 1:
    euros = float(input("Entrez le nombre d'euros que vous voulez convertir en francs: "))
    francs = euros * franc
    print(euros, "euros valent", francs, "francs")

elif choix == 2:
    euros1 = float(input("Entrez le nombre d'euros que vous voulez convertir en dollars: "))
    dollars = euros1 * dollar
    print(euros1, "euros valent", dollars, "dollars")

elif choix == 3:
    euros2 = float(input("Entrez le nombre d'euros que vous voulez convertir en livres: "))
    livres = euros2 * livre
    print(euros2, "euros valent", livres, "livres")

input("Et voilà le travail!")
