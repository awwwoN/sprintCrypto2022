#Dechiffrement Cesar
#!/usr/bin/env python3
from filter import *

log(f"Démarrage. Invoqué depuis { url }")

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
phaal = alpha[5:] + alpha[:5]
alpha += alpha.lower()
phaal += phaal.lower()
cesar = str.maketrans(phaal, alpha)
for line in input:
    output.write(line.translate(cesar))

log(f"Fin du traitement.")
