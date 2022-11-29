from math import atan2, sqrt, tan
from math import degrees as deg
from math import radians as rad

def py(c1,c2, c3): #Pythagorean Theorem
    return sqrt(c1**2 + c2**2 + c3**2)

def convertV(Vx,Vy,Vz,p,f):
    """
    POV: Px (p[0]), Py (p[1]), Pz (p[2])\n
    Frame: f[0] (Distance from P to the Frame), f[1]: Angle of frame in X, f[2]: Angle of the frame in y\n
    Vector: Vx, Vy, Vz
    """

    Dx, Dy, Dz= p[0]-Vx, p[1]-Vy, p[2]-Vz

    Ax= deg(atan2(Dz, Dx)) - f[1]
    #print('Ax:', Ax)
    x= tan(rad(Ax)) * f[0]
    

    Hy= py(Dx, Dz, Dy)
    #print('Hy:', Hy)

    Ay= deg(atan2(Dy, Hy))*-1 - f[2]
    #print('Ay:', Ay)
    y= tan(rad(Ay))*f[2]

    return((int(x),int(y)))