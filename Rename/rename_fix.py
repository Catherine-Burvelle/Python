# TP python par Catherine BURVELLE
# Buts :
#   - Découvrir les boucles
#   - Comprendre les noms de fichiers et les jockers glob
#   - Aperçu des Expressions régulières (RegEx)
#   - Utilisation de modules.

# Les imports qu'on ajoute au fur et à mesure du développement
import glob
import re
import os

# Récupération de la liste des fichiers à renommer
fileList = glob.glob('Rename/data/chaisse*.jpg')

# Boucle pour renommer chaque fichier
for file in fileList :
    # Remplacement dans la chaine de caractère de l'ancienne partie par la nouvelle
    newName=re.sub("chaisse", "chaise",file)
    # Renommage du fichier
    os.rename(file, newName)
print ("Fini")
