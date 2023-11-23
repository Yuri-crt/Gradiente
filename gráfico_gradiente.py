import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Funções:
    
    def __init__(self, x, y):
        self.pico_de_montanha = self.montanha(x, y)
        self.vulcão = self.parece_um_vulcão(x, y)
    
    def montanha(self, x, y):
        self.pico_de_montanha = (3**-(x**2 + y**2))
        return self.pico_de_montanha

    def parece_um_vulcão(self, x, y):
        self.vulcão = np.sin(np.sqrt(x**2 + y**2))
        return self.vulcão

    def gradiente_montanha(self, x, y):
        dx = -2 * x * np.log(3) * 3**-(x**2 + y**2)
        dy = -2 * y * np.log(3) * 3**-(x**2 + y**2)
        return dx, dy

    def gradiente_vulcão(self, x, y):
        r = np.sqrt(x**2 + y**2)
        dx = x * np.cos(r) / r
        dy = y * np.cos(r) / r
        return dx, dy
    
class Plot:

    def __init__(self):
        self.gráfico = plt.figure(figsize=(32, 24))

    def subplot(self, x, y, z, dx, dy, title, i):
        ax = self.gráfico.add_subplot(i, projection='3d')
        ax.plot_surface(x, y, z, cmap='terrain')
        ax.quiver(x[::3, ::3], y[::3, ::3], z[::3, ::3], dx[::3, ::3], dy[::3, ::3], 0, length=0.3, normalize=True, color='r')
        ax.set_title(title)

x = np.linspace(-3, 3, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)

f = Funções(x, y)
plot = Plot()
dx, dy = f.gradiente_montanha(x, y)
sp_mt = plot.subplot(x, y, f.pico_de_montanha, dx, dy, "Montanha: (3**-(x**2 + y**2)", 121)

dx, dy = f.gradiente_vulcão(x, y)
sp_mt = plot.subplot(x, y, f.vulcão, dx, dy, "Vulcão: sin(sqrt(x^2 + y^2))", 122)

plt.show()
