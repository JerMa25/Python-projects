#Fonction qui met une matrice dans le format CCS
def matrix_to_ccs(A):
    val = []
    row_ind = []
    col_ptr = []
    col_ptr.append(1)
    for i in range(len(A)):
        for j in range(len(A)):
            if A[j][i] != 0:
                val.append(A[j][i])
                row_ind.append(j)
        col_ptr.append(len(val) + 1)
    result = []
    result.extend([val, row_ind, col_ptr])
    return result



#Fonction qui récupère la valeur à la position [x,y] d'une matrice sous format CCS
def get(x:int,y:int,val,row_ind,col_ptr):
    
    if (x > len(col_ptr) - 2 or y > len(col_ptr) - 2):
        return "Matrix index out of range"
    
    #cas ou tous les elts de la colonne y sont nuls (en particulier a la position [x,y])
    if col_ptr[y+1] - col_ptr[y] == 0:
        return 0
    
    #[col_ptr[y]-1,col_ptr[y+1]-1] : intervalle d'indice dans lequel se trouve la valeur recherche dans le vecteur val
    for i in range(col_ptr[y] - 1 , col_ptr[y + 1] - 1):
        if (x == row_ind[i]):
            return val[i]
    return 0



#Fonction qui place une valeur a à la position [x,y] d'une matrice sous format CCS
def set(x:int,y:int,a,val,col_ptr,row_ind):
    
    #cas où la valeur à inserer et celle à la position d'inserion sont les mêmes
    if get(x,y,val,col_ptr,row_ind) == a:
        return(val, row_ind, col_ptr)
    
    #cas où la valeur à insérer est différente de 0 et que les valeurs sur la ligne d'insertion sont toutes nulles
    #(En particulier à la position d'insertion) 
    if col_ptr[y+1] - col_ptr[y] == 0 and a != 0:
        val.insert(col_ptr[y] - 1, a)
        row_ind.insert(col_ptr[y] - 1, y)
        for i in range(y+1, len(col_ptr)):
            col_ptr[i] += 1
        return(val, row_ind, col_ptr)
    
    #cas où la valeur à insérer est nulle et que la valeur à la position d'insertion est non nulle
    if a == 0:
        val.pop(col_ptr[y] + x - 1)
        row_ind.pop(col_ptr[y] + x - 1)
        for i in range(y+1, len(col_ptr)):
            col_ptr[i] -= 1
        return(val, row_ind, col_ptr)
    
    #cas où la valeur à insérer est non nulle et que la valeur à la position d'insertion est non nulle
    val[col_ptr[y] + x - 1] = a
    return(val, row_ind, col_ptr)


#Phase de test
A = [[1,2,3],[3,-1,3],[4,0,-2]]
A = matrix_to_ccs(A)
print(A)
val = A[0]
row_ind = A[1]
col_ptr = A[2]
print(val)
print(row_ind)
print(col_ptr)
print(get(2, 2, val, row_ind, col_ptr))
  