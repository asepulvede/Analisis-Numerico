!pip install sympy
import sympy as sp
import numpy as np
from sympy import *
import math
x= symbols('x')

def secante(fx,x0,xf,maxI,tol):
  cont=0
  error=tol+1
  while cont<maxI and error>tol:
    xn= x0-fx.subs(x,x0)*(xf-x0)/(fx.subs(x,xf)-fx.subs(x,x0))
    error= abs(xn-x0)
    xf=x0
    x0=xc
    cont= cont+1
  if error<tol:
    print(xn,'es raiz con tolerancia',tol)
  else:
    print('no hay raiz')
