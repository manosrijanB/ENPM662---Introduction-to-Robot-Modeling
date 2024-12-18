from sympy import *
import matplotlib.pyplot as plt
from math import radians
import numpy as np

#symbols for the robot joints
theta = IndexedBase('theta')
alpha = symbols('alpha')
a, d = symbols('a, d')

#gravity
g = 9.8
#mass of the robot links
m_hand = 0.73
m_left_finger = 0.1
m_right_finger = 0.1
m = [3.06, 4.97, 0.65, 3.23, 3.59, 1.23, 1.67, 0.74, (m_hand + m_left_finger + m_right_finger)]

# parameters for the robot links
thetas = [theta[1], theta[2], theta[3], theta[4], theta[5], theta[6], theta[7]]
alphas = [np.pi/2, -np.pi/2, -np.pi/2, np.pi/2, -np.pi/2, np.pi/2, 0]
d_s = [0.3330, 0, 0.3160, 0, 0.3840, 0, -0.2070]
a_s = [0, 0, 0.0880, 0, -0.0880, 0.0880, 0]


# general homogeneous transformation:
def trans_mat(theta, alpha, d, a):
    return Matrix(([cos(theta), -sin(theta)*cos(alpha),  sin(theta)*sin(alpha), a*cos(theta)],
                   [sin(theta),  cos(theta)*cos(alpha), -cos(theta)*sin(alpha), a*sin(theta)],
                   [0, sin(alpha), cos(alpha), d],
                   [0, 0, 0, 1]))

# transformation matrices for each joint in the robot
T = [trans_mat(thetas[i], alphas[i], d_s[i], a_s[i]) for i in range(7)]
# transformation matrices for each joint in the robot from base to end effector
for i in range(1, 7): T[i] = T[i-1] * T[i]


# effector position from T7
Fwd_Kin = T[-1][:3, 3]
# Jacobian 
Jac_v = Fwd_Kin.jacobian(thetas)
Jac_w = Matrix.hstack(*[T[i][:3, 2] for i in range(7)])
Jacobian = Jac_v.col_join(Jac_w)
Jacobian = lambdify(thetas, Jacobian, 'numpy')
Fwd_Kin  = lambdify(thetas, Fwd_Kin, 'numpy')

#initial joint angles
q_curr = np.array([0, 0, 0, np.pi/2, 0, np.pi, 0])

t, w = 0, 0.1
num_points = 100
total_time = 2*np.pi/w
dt = total_time/num_points

Xp = []
joint_torques = []
for _ in range(num_points):
    # Jacobian
    J_sub = Jacobian(*q_curr)
    J_inv = np.linalg.pinv(J_sub)
    # Forward Kinematics
    Xp_t = Fwd_Kin(*q_curr)
    Xp.append(Xp_t)
    # update joint angles
    x_dot = np.array([0, 0.1*w*np.sin(w*t + np.pi/2), 
                         0.1*w*np.cos(w*t + np.pi/2), 
                      0, 0, 0])
    q_dot = J_inv @ x_dot
    q_curr += q_dot*dt
    t += dt

# convert to numpy array
Xp = np.array(Xp)

# plot the end effector position
plt.plot(Xp[:, 1], Xp[:, 2], 'r.')
plt.xlabel("z")
plt.ylabel("y")
plt.savefig("HW4.png")
plt.show()
