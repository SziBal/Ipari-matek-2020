import random
import matplotlib.pyplot as plt

def ran():
    rand=[-1,1]
    list=random.choices(rand,k=1000)
    list2=[]
    a=0
    for x in range(100):
        a+=list[x]
        list2.append(a)
    print(list)
    print(list2)
    plt.plot(range(100),list2)
    plt.show()
