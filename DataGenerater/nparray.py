import numpy as np
import array
a=np.array([[1,2,3,4],[4,4,4,4]])
b=np.array(a[1,:])
print(type(a[1,:]))
print(a)
print(b)
c=[1,1,2,3,4,5]
print(c+c)
print(type(c+c))
d=np.array(c+c)
print(d)
print(type(d))
e = np.zeros((8, 8))
print(d.tolist())
print(type(d.tolist()))