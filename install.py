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