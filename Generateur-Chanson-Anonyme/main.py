from synonymes import linternaute
parole = input("Entrez vos paroles ici :\n")
new = []

for mot in parole.split(" "):
    new_mot = linternaute(mot)
    if len(new_mot)<1:
        new.append(mot)
    else:
        new.append(new_mot[0])