#my logic for interplation newton
import sympy
from sympy.plotting import plot



def newton_interplation(vect_x,vect_y,degree):
    x = sympy.symbols("x")
    f = vect_y[0]
    for  j in range(1,degree+1):
        vect = []
        for i in range(len(vect_y)-1):
            vect.append((vect_y[i]-vect_y[i+1])/(vect_x[i]-vect_x[i+j]))##newton coeff
        produit=1
        for k in range(0,j):
            produit=produit*(x-vect_x[k])
        f=f+produit*vect[0]
        vect_y=vect
    final_function_without_error=f #--->le polynome d’interpolation dans la base de Newton
    plot_function=plot(final_function_without_error)
    print(plot_function) #----> plot 
    print(final_function_without_error) #
newton_interplation([0,2,4],[1,5,17],2)
