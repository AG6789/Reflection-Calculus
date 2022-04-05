from sympy import * 
from math import atan, tan
import matplotlib.pyplot as plt
import numpy as np
import sys


x, y = symbols('x y')

mirror = input("Enter equation of mirror in a*x**m + b*y**n + c (mirror has to be a curve, '= 0' is taken automatically.) format: ")
iray = input("Enter equation of incident ray in a*x + b*y + c (iRay has to be a line, '= 0' is taken automatically.) format: ")

def findAngle(M1, M2):
    
    PI = 3.14159265
    
    try:
        angle1 = atan(M1)
        angle2 = atan(M2)
        angle = abs(angle1 - angle2)
        val = (angle * 180) / PI
        return (round(val))
    
    except:
        sys.exit("Incident ray is tangential to mirror. Reflected ray has same equation. (Or you've entered wrong numbers).")
        
def findSlope(angle, M1):
    
    PI = 3.14159265
    
    angle1 = atan(M1)
    angle2 = (angle*PI)/180
    angle3 = angle1 - angle2
    M2 = tan(angle3)
    
    return round(M2)

eq1 = Eq(eval(mirror), 0)
eq2 = Eq(eval(iray), 0)

solution = (solve((eq1,eq2), (x, y)))

while(len(solution) > 1):
    solution.pop(0)

solutionList = list(solution[0])

mirror_diff = Derivative(mirror, x) 
diff_mirror = list("{}".format(mirror_diff.doit()))

x1 = solutionList[0]
y1 = solutionList[1]

for i in range(len(diff_mirror)):
    if diff_mirror[i] == "x":
        diff_mirror[i] = str(x1)
        
    if diff_mirror[i] == "y":
        diff_mirror[i] = str(y1)

diff_mirror_final = eval(''.join(diff_mirror))

i_diff = Derivative(iray, x) 
diff_i = list("{}".format(i_diff.doit()))

for i in range(len(diff_i)):
    if diff_i[i] == "x":
        diff_i[i] = str(x1)
        
    if diff_i[i] == "y":
        diff_i[i] = str(y1)

diff_i_final = eval(''.join(diff_i))


tanconst = y1 - diff_mirror_final*x1
irayconst = y1 - diff_i_final*x1

slope_normal = -1/diff_mirror_final
normalconst = y1 - slope_normal*x1

angleNormal = findAngle(diff_i_final, slope_normal)
slope_reflected = findSlope(angleNormal, slope_normal)

reflected_const = y1 - slope_reflected*x1

print("\n")
print(f"The equation of the reflected ray is: y = {slope_reflected}x + {reflected_const}.")
print(f"The incident ray will strike the mirror at {solutionList}.")
print(f"The angle of incidence and reflection is {angleNormal}.")






    

        

