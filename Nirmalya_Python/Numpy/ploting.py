import numpy as np
import matplotlib.pyplot as plt

#ploting sin wave
x_plot = np.arange(0, 3*np.pi, 0.1)
y_plot = np.sin(x_plot)
y_plot_cos = np.cos(x_plot)

# subplot
plt.subplot(2,1,1)
plt.plot(x_plot,y_plot)
plt.title("Sin wave")

plt.subplot(2,1,2)
plt.plot(x_plot,y_plot_cos)
plt.title("Cosine wave")

plt.plot(x_plot, y_plot)
plt.plot(x_plot, y_plot_cos)

plt.xlabel("X Aixis")
plt.ylabel("Y Label")
plt.title("Sin and Cosine")
plt.legend(['Sin', 'Cosine'])
plt.show()

x_parabola = np.linspace(-20,20,100)
y_parabola = x_parabola**2
y_curve = 5*(x_parabola**2) + 6*x_parabola + 3
y_curve2 = 1 - ((x_parabola**2)/2)

plt.subplot(3,1,1)
plt.plot(x_parabola, y_parabola)
plt.title("Parabola")

plt.subplot(3,1,2)
plt.plot(x_parabola, y_curve)
plt.title("curve1")

plt.subplot(3,1,3)
plt.plot(x_parabola, y_curve2)
plt.title("curve2")
plt.show()