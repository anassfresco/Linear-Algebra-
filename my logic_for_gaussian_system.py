#Triangular matrix
import numpy as np
a=np.array([[1,2,3],[2,6,12],[4,12,6]])
b=np.array([3,2,1])

for k in range(0,a.shape[1]):
    for i in range(k + 1, a.shape[0]):
        matrice = a[k] * a[i][k] // a[k][k]
        vect = b[k] * a[i][k] // a[k][k]

        a[i] = a[i] - matrice
        b[i] = b[i] - vect
#gaussian systeme 
def gausaian_system(matrice,vector):
    i=matrice.shape[0]-1
    help_matrice=np.array([1]*(i+1))
    while i>=0:
        sum_matrice=help_matrice*matrice[i]
        help_matrice[i]=(vector[i]-sum(sum_matrice[i+1::]))// matrice[i][i]
        i=i-1
    return help_matrice
print(gausaian_system(a,b))
