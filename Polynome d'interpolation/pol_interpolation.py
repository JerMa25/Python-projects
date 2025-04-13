from Schemas_de_Horner import horner_Newton

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

def pol(a,f):
    coeff = piL(a,f)
    def P(x):
        return horner_Newton(len(a)-1,x,a,coeff)
    return P
