import json
import os


print("Pico Linux 0.1")

with open("./etc/passwd.json", "r") as f:
    compte = json.load(f)

utilisateur = input("utilisateur: ")
mdp = input("mdp: ")

while utilisateur != compte["utilisateur"] and mdp != compte["mdp"]:
    print("Veuillez réessayer")
    utilisateur = input("utilisateur: ")
    mdp = input("mdp: ")

dossier_utilisateur = f"./home/{utilisateur}"
dossier_actuel = dossier_utilisateur

with open("./directory.json", "w") as f:
    json.dump(dossier_actuel, f)

while True:
    commande = input(f"{utilisateur}-Pico-Linux$ ")

    if os.path.exists(f"./bin/{commande}.py"):
        exec(open(f"./bin/{commande}.py").read())
    
    else:
        print("commande inconnu")