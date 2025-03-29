#Fonction qui met une matrice sous format CRS
def matrix_to_crs(A):
    val = []
    col_ind = []
    row_ptr = []
    row_ptr.append(1)
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] != 0:
                val.append(A[i][j])
                col_ind.append(j)
        row_ptr.append(len(val) + 1)
    result = []
    result.extend([val, col_ind, row_ptr])
    return result



#Fonction qui récupère la valeur à la position [x,y] d'une matrice sous format CRS
def get(x:int, y:int, val, col_ind, row_ptr):
    
    if (x > len(row_ptr) - 2 or y > len(row_ptr) - 2):
        return "Matrix index out of range"
    
    #cas ou tous les elts de la colonne y sont nuls (en particulier a la position [x,y])
    if row_ptr[x + 1] - row_ptr[x] == 0:
        return 0
    
    #[row_ptr[x]-1,row_ptr[x+1]-1] : intervalle d'indice dans lequel se trouve la valeur recherche dans le vecteur val
    for i in range(row_ptr[x] - 1, row_ptr[x + 1] - 1):
        if (y == col_ind[i]):
            return val[i]
    return 0



#Fonction qui place une valeur a à la position [x,y] d'une matrice sous format CRS
def set(x:int, y:int, a, val, col_ind, row_ptr):
    
    #cas où la valeur à inserer et celle à la position d'insertion sont les mêmes
    if get(x, y, val, row_ptr, col_ind) == a:
        return(val, col_ind, row_ptr)
    
    #cas où la valeur à insérer est différente de 0 et que les valeurs sur la ligne d'insertion sont toutes nulles
    #(En particulier à la position d'insertion) 
    if row_ptr[x + 1] - row_ptr[x] == 0 and a != 0:
        val.insert(row_ptr[x] - 1, a)
        col_ind.insert(row_ptr[x] - 1, x)
        for i in range(x + 1, len(row_ptr)):
            row_ptr[i] += 1
        return(val, col_ind, row_ptr)
    
    #cas où la valeur à insérer est nulle et que la valeur à la position d'insertion est non nulle
    if a == 0:
        val.pop(row_ptr[x] + y - 1)
        col_ind.pop(row_ptr[x] + y - 1)
        for i in range(x+1, len(row_ptr)):
            row_ptr[i] -= 1
        return(val, col_ind, row_ptr)
    
    #cas où la valeur à insérer est non nulle et que la valeur à la position d'insertion est non nulle
    val[row_ptr[x] + y - 1] = a
    return(val, col_ind, row_ptr)



#Fonction qui effectue le produit d'une matrice sous format CRS avec un vecteur quelconque
def prodMatVectcrs(val, col_ind, row_ptr, vect):
    result = []
    if len(vect) == len(row_ptr) - 1:
        for i in range(len(row_ptr) - 1):
            a = 0
            for j in range(row_ptr[i] - 1, row_ptr[i + 1] - 1):
                a += val[j] * vect[col_ind[j]]
            result.append(a)                
    return result



#Phase de test
A = [[1,2,3],[3,-1,3],[4,0,-2]]
A = matrix_to_crs(A)
val = A[0]
col_ind = A[1]
row_ptr = A[2]
print("val:",val)
print("col_ind:",col_ind)
print("row_ptr:",row_ptr)
print(get(2, 1, val, col_ind, row_ptr))
print(set(0,0,5,val,col_ind,row_ptr))
print(prodMatVectcrs(val, col_ind, row_ptr, [1,1,1]))