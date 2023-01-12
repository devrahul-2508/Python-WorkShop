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