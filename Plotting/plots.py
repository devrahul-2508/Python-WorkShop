import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(0,3*np.pi,0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# #Creating the first plot
# plt.subplot(2,1,1)
# plt.plot(x,y_sin)
# plt.title("Sin Wave")

# #Creating the second plot
# plt.subplot(2,1,2)
# plt.plot(x,y_cos)
# plt.title("Cos Wave")

# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.show()

x_para = np.arange(-4,5,1)
y_para = np.square(x_para);
plt.subplot(3,1,1)
plt.plot(x_para,y_para)

x_expo = np.arange(0,5,1)
y_expo = 5*x_expo**2+6*x_expo+3
plt.subplot(3,1,2)
plt.plot(x_expo,y_expo)

x_t = np.arange(0,5,1)
y_t = 1- x_t**2/2
plt.subplot(3,1,3)
plt.plot(x_t,y_t)
plt.show()


