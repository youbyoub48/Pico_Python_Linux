# sourcery skip: do-not-use-bare-except
import json


print("Pico Linux 0.1")

with open("./etc/passwd.json", "r") as f:
    compte = json.load(f)

utilisateur = input("utilisateur: ")
mdp = input("mdp: ")

while utilisateur != compte["utilisateur"] or mdp != compte["mdp"]:
    print("Veuillez réessayer")
    utilisateur = input("utilisateur: ")
    mdp = input("mdp: ")

dossier_utilisateur = f"./home/{utilisateur}"
dossier_actuel = dossier_utilisateur

with open("./directory.json", "w") as f:
    json.dump(dossier_actuel, f)

boucle = True

while boucle:
    commande = input(f"{utilisateur}-Pico-Linux$ ")
    commande = commande.split(" ")

    if commande[0] == "exit":
            boucle = False

    try:
        if len(commande) > 1:
            with open("./argument.json", "w") as f:
                json.dump(commande[1], f)
        exec(open(f"./bin/{commande[0]}.py").read())

    except:
        if commande != "":
            print("commande inconnu")