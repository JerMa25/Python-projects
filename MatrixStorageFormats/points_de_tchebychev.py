from math import acos, cos, pi, degrees

def pts_tchebychev(a,b,degree:int):
    points = []
    for k in range(degree):
        points.append((a + b)/2 + ((b - a)/2) * cos((2 * k + 1) * pi/(2 * degree)))
    return points