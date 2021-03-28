print("hello world")
a=[]
d=[]
arr=[]
import random
for i in (list(range(1000))):
    b=random.randint(1,6)
    c=random.randint(1,6)
    a.append(b)
    d.append(c)
    sb=str(b)
    sc=str(c)
    s=("["+sb+","+sc+"]")
    arr.append(s)
print (a)
import numpy
from numpy import *
import pylab
from pylab import *    
import matplotlib
from matplotlib import *
print("CHECK")
fig=plt.figure(figsize=(8,8))
his=fig.add_axes([0,0,1,1])
plt.hist(arr,bins=100)
plt.show()
print(s)    


