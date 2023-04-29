from os import system
while True:
    operation = input("Entrez une opération :\n")

    #Remplacement des signes :

    operation = operation.replace("x", "*")

    print(eval(operation))
    system("cls")