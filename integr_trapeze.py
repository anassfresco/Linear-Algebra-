def my_function(x):
    return x**2 #example for f(x)=x**2

def trapeze(a,b,n):
    integr=0
    for i in range(1,n):
        integr=my_function(a+i*((b-a)/n))
    integr=integr*2+my_function(0)
    integr+=my_function(n)
    integr*=(((b-a)/n)/2)
    print(integr)
trapeze(0,100,4)
