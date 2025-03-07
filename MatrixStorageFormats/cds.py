#Fonction qui récupère la valeur à la position [x,y] d'une matrice sous format CRS
def get(i, j, VAL):
    return VAL[j - i + len(VAL[0]) - 1][i]

#Phase de test
VAL = [[0,0,4],[0,3,5],[1,-1,-2],[2,3,0],[3,0,0]]
print(get(1, 1, VAL))