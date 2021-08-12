from matplotlib import pyplot as plt
def rung_kutta_range_4(h,n,t0):
    somme=t0
    array=[t0]
    for i in range(1,n):
        k1=(diff(somme,h/i))
        k2=(diff(somme+h/2*k1,h/i+h/2))
        k3=diff(somme+h/2*k2,h/n+h/2*k2)
        k4=diff(somme+h*k3,h/n+h/2)
        somme=somme+h/6*(k1+2*k2+2*k3+k4)
        array.append(somme)
    return array

x=euler(0.5,16,5)
y=list(range(len(x)))
new_x=rung_kutta_range_4(0.5,16,5)
plt.plot(x,y,"r")
plt.plot(new_x,y,"b")
plt.show()
