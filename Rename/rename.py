
# TP python par Catherine BURVELLE
# Buts :
#   - Découvrir les boucles
#   - Comprendre les noms de fichiers et les jockers glob
#   - Aperçu des Expressions régulières (RegEx)
#   - Utilisation de modules.

import glob
import re
import os
import sys

# On compte le nombre d'argument sur la ligne de commande
# argv[0] contient le nom du script donc on n'en tient pas compte
nbArg = len(sys.argv) - 1
if nbArg < 4 :
    directory = input("Répertoire où se trouvent les fichiers : ")
    jocker = input("Jocker pour reconnaître les fichiers : ")
    needle = input("Partie du nom à remplacer : ")
    replacement = input("Valeur de remplacement : ")
else :
    directory = sys.argv[1]
    jocker = sys.argv[2]
    needle = sys.argv[3]
    replacement = sys.argv[4]

# Le nom du répertoire doit se terminer avec unslash avent d'y rajouter le jocker
if not directory.endswith('/') :
    directory += '/'

# Liste des fichiers correspondant au jocker dans le répertoire donné
fileList = glob.glob(directory + jocker)

# Boucle pour renomer les fichiers chacun à leur tour
for file in fileList :
    # Remplacement dans le nom de la mauvaise partie par la bonne
    newName=re.sub(needle, replacement, file)
    # J'affiche à l'écran ce que je fais pour que tu ne sois pas perdu ;-)
    print ("Renomage de " + file + " en " + newName)
    # Renomage du fichier
    os.rename(file, newName)

# Et voilà !
print ("Fini")
