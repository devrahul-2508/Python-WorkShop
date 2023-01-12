import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20,20,100)
# def func(x):
#     y = []
#     for elem in x:
#         result = elem**2
#         y.append(result)
#     return y    

y=np.square(x)
plt.plot(x,y)
plt.show()        
