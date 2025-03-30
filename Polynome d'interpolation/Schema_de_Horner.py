def horner(n,x,coeff):
    y = coeff[n]
    for k in range(n-1,-1,-1):
        y = y * x + coeff[k]
    return y

def horner_Newton(n,x,a,coeff):
    y = coeff[n]
    for k in range(n-1,-1,-1):
        y = y * (x - a[k+1]) + coeff[k]
    return y

def horner_Taylor(n,x,a,coeff):
    y = coeff[n]
    for k in range(n-1,-1,-1):
        y = y * ((x - a[k+1])/(k + 1)) + coeff[k]
    return y

def horner_TaylorCentree(n,x,a0,coeff):
    y = coeff[n]
    t = x-a0
    for k in range(n-1,-1,-1):
        y = y * (t/(k + 1)) + coeff[k]
    return y
