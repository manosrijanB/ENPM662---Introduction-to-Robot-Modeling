from sympy import *
import matplotlib.pyplot as plt
from math import radians
import numpy as np

#symbols for the robot joints
theta = IndexedBase('theta')
alpha = symbols('alpha')
a, d = symbols('a, d')

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
for i in range(1, 7): 
    T[i] = T[i-1] * T[i]

T_f = lambdify(thetas, T[-1], 'numpy') 
# print the transformation matrices
# for i in range(7): 
#     pprint(nsimplify(T[i], tolerance=1e-10, rational=True).evalf())

configs = [[0, 0, 0, 0, 0, 0, 0],
           [np.pi/2, 0, 0, 0, 0, 0, 0],
           [0,-np.pi/2, 0, 0, 0, 0, 0],
           [0, 0, 0, np.pi/2, 0, 0, 0],
           [0, 0, 0, np.pi/2, 0, np.pi/2, 0]]

for i in range(5):
    print("config: ", i)
    print(np.round(T_f(*configs[i]), 2))
