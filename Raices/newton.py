!pip install sympy
import sympy as sp
import numpy as np
from sympy import *
import math
from math import *
x= symbols('x')

def newton(fx,x0,maxI,tol):
  fd= diff(fx)
  cont=0
  error= tol+1
  while cont<maxI and error>tol:
    xn= x0-fx.subs(x,x0)/fd.subs(x,x0)
    error= abs(xn-x0)
    cont= cont+1
    x0=xn
  if error<=tol:
    print(xn,'es raiz con tolerancia',tol)
  else:
    print('no converge')
  
newton(x**3-(1/(sqrt(2))*x**2-5*5),2,20,0.0000005)
