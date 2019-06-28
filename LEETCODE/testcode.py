import math
from numpy import cross, eye, dot
from scipy.linalg import expm, norm

def M(axis, theta):
    return expm(cross(eye(3), axis/norm(axis)*theta))

v, axis, theta = [4,4,4], [0,0,1], np.(math.pi/2.0)
M0 = M(axis, theta)

print(dot(M0,v))