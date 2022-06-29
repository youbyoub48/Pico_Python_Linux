import json

with open("./argument.json", "r") as f:
    dossier = json.load(f)

dossier = "."+dossier
with open("./directory.json", "w") as f:
    json.dump(dossier,f)