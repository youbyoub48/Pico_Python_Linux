import os, json

fichier = ""

with open("./directory.json", "r") as f:
    dossier = json.load(f)

for element in os.listdir(dossier):
    fichier = f"{fichier} {element}"

print(fichier)