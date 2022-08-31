!pip install sympy
import sympy as sp
import numpy as np
from sympy import *
import math
x= symbols('x')

def raices_mul(fx,x0,maxI,tol): 
  ux= fx/diff(fx)
  uxx= diff(ux)
  cont=0
  error= tol+1
  while cont<maxI and error>tol:
    xn= x0-ux.subs(x,x0)/uxx.subs(x,x0)
    error= abs(xn-x0)
    cont= cont+1
    x0=xn
  if error<=tol:
    print(xn,'es raiz con tolerancia',tol)
  else:
    print('no converge')

raices_mul(x**2-1,-1,20,0.05)
