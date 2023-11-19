import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
from matplotlib import cm

def trajectory_general(x, y, xdot, ydot, f, fdot, eps=0.01):

    elasticity = 1

    scalar = -fdot(x)*xdot + ydot
    norm = np.sqrt(1+fdot(x)**2)

    bit = 1/4 * (1 - np.sign(y-f(x)-eps))*(1 - np.sign(scalar))

    F_grav = g/norm
    Factor_v = 2*scalar/(norm**2)

    xdotdot = bit*((elasticity * (xdot + Factor_v * fdot(x) ) - xdot)/dt + F_grav * (-fdot(x)))
    ydotdot = bit*((elasticity * (ydot - Factor_v ) - ydot)/dt + F_grav) - g


    return (xdotdot, ydotdot)

def trajectory_negbell(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: -np.exp(-1*(t**2)), lambda t: 2*t*np.exp(-1*(t**2)))

def trajectory_bell(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: np.exp(-1*(t**2)), lambda t: -2*t*np.exp(-1*(t**2)))

def trajectory_diag(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: -0.25*t, lambda t: -0.25)

def trajectory_square(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: t**2, lambda t: 2*t)

def trajectory_sine(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: np.sin(t), lambda t: np.cos(t))

def trajectory_flat(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: 0, lambda t: 0)

def trajectory_cosh(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: np.cosh(t), lambda t: np.sinh(t))

def trajectory_flatter_cosh(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: np.cosh(t) + np.cos(t), lambda t: np.sinh(t) - np.sin(t))

def trajectory_abs(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: np.abs(t), lambda t: np.sign(t))

def trajectory_bowl(x, y, xdot, ydot):
    return trajectory_general(x, y, xdot, ydot, lambda t: -np.sqrt(1-t**2) +1, lambda t: t/np.sqrt(1-t**2))

g=9.81
mass = 1

dt = 0.001
t_start = 0
t_end = 5
nBalls = 50000

#Rectangle to mask later
rect_width = 0.5
rect_height = 0.5
origin = (0, 2.1)

x_grid, y_grid = np.meshgrid(np.linspace(origin[0]-rect_width, origin[0]+rect_width, int(np.sqrt(nBalls))), np.linspace(origin[1]-rect_height, origin[1]+rect_height, int(np.sqrt(nBalls))))

mask_heart = (4*x_grid)**2 + (5.12*(y_grid-2) - 4*np.abs(x_grid))**2 <= 1
#mask_cosh = (np.cosh(x_grid) + 1 - y_grid <= 0) & (y_grid <= 3)
#mask_diamond = np.abs(x_grid*(y_grid-2))**1.2 + np.abs(x_grid)**1.2 + np.abs((y_grid-2))**1.2 <= 0.3

xBalls = x_grid[mask_heart]
yBalls = y_grid[mask_heart]

print(len(xBalls), "points used for the initial shape")

U_list = np.array([[xBalls[i], 0, yBalls[i], 0] for i in range(len(xBalls))])
colors = cm.rainbow(np.linspace(0, 1, len(U_list)))
fig, ax = plt.subplots()
axis = [-2,2,-0.2,3.2]
x_axis = np.arange(axis[0],axis[1], dt)

ax.axis(axis)
ax.set_aspect("equal")

#Plot the actual function
ax.plot(x_axis, np.abs(x_axis))

points = ax.scatter(U_list[:,0], U_list[:,2], s=10, c=colors)
speedUp = 1
print("SpeedUp:",speedUp)


def update(t):
    for AAAA in range(speedUp):
        for j in range(len(U_list)):
            prev_x = U_list[j][0]
            prev_xdot = U_list[j][1]
            prev_y = U_list[j][2]
            prev_ydot = U_list[j][3]
            prev_xdotdot, prev_ydotdot = trajectory_abs(prev_x, prev_y, prev_xdot, prev_ydot)
            U_list[j][0:] = [dt * prev_xdot + prev_x, dt * prev_xdotdot + prev_xdot, dt * prev_ydot + prev_y,
                      dt * prev_ydotdot + prev_ydot]
    points.set_offsets(np.column_stack((U_list[:,0], U_list[:,2])))
    if t % int((t_end/(dt*speedUp))/100) == 0:
        print(t, "out of", int(t_end/(dt*speedUp)), "(" + str(round(t*100/int(t_end/(dt*speedUp)), 3)) + "%)")
    return points,

ani = FuncAnimation(fig, update, interval=1, blit=True, frames=int(t_end/(dt * speedUp)))

writervideo = FFMpegWriter(fps=int(0.5/(speedUp*dt)))
ani.save('Cool_ball.mp4', writer=writervideo)