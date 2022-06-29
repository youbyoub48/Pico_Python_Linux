import os, json

dossier = ["./bin","./boot","./dev","./etc","./etc/X11","./etc/opt","./home","./lib","./mnt","./opt","./root","./sbin","./tmp","./usr","./usr/X11R6","./usr/X386","./usr/bin","./usr/include","./usr/lib","./usr/local","./usr/local/bin","./usr/local/games","./usr/local/include","./usr/local/lib","./usr/local/sbin","./usr/local/share","./usr/local/src","./usr/sbin","./usr/share","./usr/src","./var"]

for element in dossier:
    if not os.path.exists(element):
        os.mkdir(element)

utilisateur = input("Choisisez un nom d'utilisateur: ")
mdp = input("mdp: ")
compte = {"utilisateur": utilisateur, "mdp": mdp}

with open("./etc/passwd.json","w") as f:
    json.dump(compte, f)

os.mkdir(f"./home/{utilisateur}")

main = """
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
"""

with open("main.py", "w") as f:
    f.write(main)