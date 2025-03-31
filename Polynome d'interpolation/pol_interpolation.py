def piL(a,f):
    T,coeff = [],[]
    for i in range(len(f)):
        T.append([])
        T[i].append(f[i])
    for j in range(1,len(f)):
        for i in range(j,len(f)):
            T[i].append((T[i][j-1] - T[i-1][j-1])/(a[i] - a[i-j]))
    for i in range(len(f)):
        coeff.append(T[i][i])
    return coeff
