import numpy as np
import matplotlib.pyplot as plt

# veichle Constants
wheel_dia= 0.5
chassis_length = 4
wheel_distance = 1.5
wheel_radius = wheel_dia/ 2

def state_dot(x, u):
    
    # writing a function for State-space model 
    
    w, alpha = u
    x_dot = np.array([
        w * np.cos(x[2]),
        w * np.sin(x[2]),
        w * np.tan(alpha) / wheel_distance
    ])
    return x_dot

def trajectory(x_i, y_i, phi_i, w, alpha, T):
    
    # function for calculating the trajectory
    
    dt = 0.1
    x = np.array([x_i, y_i, phi_i])
    u = np.array([w, alpha])
    xs, ys = [], []
    for i in range(int(T/dt)):
        x += state_dot(x, u) * dt
        xs.append(x[0])
        ys.append(x[1])
    return xs, ys
# taking arbitrary 
def main():
    # Initial pose
    x_i = 0.0
    y_i = 0.0
    phi_i = 0.0

    # Drive speed
    w = 1

    # Steering angle(change this to change the trajectory plot)
    alpha =20*np.pi/180

    # Duration
    T = 10

    #plot trajectory
    xs, ys = trajectory(x_i, y_i, phi_i, w, alpha, T)
    plt.plot(xs, ys)
    plt.show()

if __name__ == '__main__':
    main()
