# TP python par Catherine BURVELLE
# Buts :
#   - Découvrir les boucles
#   - Comprendre les noms de fichiers et les jockers glob
#   - Aperçu des Expressions régulières (RegEx)
#   - Utilisation de modules.

import glob
import re
import os

fileList = glob.glob('Rename/data/chaisse*.jpg')

for file in fileList :
    newName=re.sub("chaisse", "chaise",file)
    os.rename(file, newName)
print ("Fini")
