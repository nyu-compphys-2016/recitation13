import matplotlib.pyplot as plt
import numpy as np



def f(x, y, t, k=1.0, w=1.0):

    r1 = np.sqrt((x+0.5)*(x+0.5)+y*y)
    r2 = np.sqrt((x-0.5)*(x-0.5)+y*y)

    return np.cos(k*r1-w*t) - np.cos(k*r2-w*t)

Nx = 100
Ny = 200

ax = -1.0
bx = 1.0
ay = 0.0
by = 5.0

xf = np.linspace(ax, bx, Nx+1)
yf = np.linspace(ay, by, Ny+1)

x = 0.5*(xf[1:] + xf[:-1])
y = 0.5*(yf[1:] + yf[:-1])

k = 10
w = 1.0


t = np.linspace(0.0, 3 * 2*np.pi/w, 100)

for i in range(len(t)):

    print(i)

    F = f(x[:,None], y[None,:], t[i], k=k, w=w)

    fig, ax = plt.subplots(1,1, figsize=(9,12))
    #C = ax.imshow(F.T, origin='lower')
    #ax.contour(x, y, F.T)
    #C = ax.contourf(x, y, F.T, 256, cmap=plt.cm.afmhot)
    C = ax.pcolormesh(xf, yf, F.T, cmap=plt.cm.inferno)
    ax.set_aspect('equal')
    fig.colorbar(C)
    
    fig.suptitle("t = {0:.3g}".format(t[i]))

    fig.savefig("{0:s}_{1:03d}.{2:s}".format("plot",i,"png"))

    plt.close(fig)



