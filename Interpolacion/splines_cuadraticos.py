import numpy as np

def splinesCuadraticos(xy):
  rows, columns= xy.shape
  x= xy[:,0]
  y= xy[:,1]
  y1= y.copy()
  x1= x.copy()

  y2= np.concatenate((y,y1))
  y2= np.sort(y2)
  x2= np.concatenate((x,x1))
  x2= np.sort(x2)

  A= np.zeros(((len(x)-1)*3-1,(len(x)-1)*3-1))
  b1= np.zeros((len(y)*2-2))
  xx= np.zeros((len(y)*2-2))
  b2= np.zeros((len(y)-2))

  for i in range(len(b1)):
    b1[i]= y2[i+1]
    xx[i]= x2[i+1]
  print(xx)

  b=np.concatenate((b1,b2))
  print(b)

splinesCuadraticos(np.array([[1,2],[3,4],[5,6],[7,8]]))
