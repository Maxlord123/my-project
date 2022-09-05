from cmath import sqrt
from math import *


def max(a, b, c):
    
    e1=-b+sqrt(b**2-4*a*c)/2*a
    e2=b+sqrt(b**2-4*a*c)/2*a
    
    

    print(f"x1={e1}, \nx2={e2}")

       
max(3, 10, 3)