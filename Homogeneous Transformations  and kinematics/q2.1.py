

import numpy as np
from math import radians
import matplotlib.pyplot as plt

psi, theta, phi = radians(35), (15), (20)
omega_max = radians(1)

#make rotation matrix from the given angles
R = np.zeros((3,3))
R[0,0] = np.cos(phi)*np.cos(theta)
R[0,1] = np.cos(phi)*np.sin(theta)*np.sin(psi) - np.sin(phi)*np.cos(psi)
R[0,2] = np.cos(phi)*np.sin(theta)*np.cos(psi) + np.sin(phi)*np.sin(psi)
R[1,0] = np.sin(phi)*np.cos(theta)
R[1,1] = np.sin(phi)*np.sin(theta)*np.sin(psi) + np.cos(phi)*np.cos(psi)
R[1,2] = np.sin(phi)*np.sin(theta)*np.cos(psi) - np.cos(phi)*np.sin(psi)
R[2,0] = -np.sin(theta)
R[2,1] = np.cos(theta)*np.sin(psi)
R[2,2] = np.cos(theta)*np.cos(psi)


trace = np.trace(R)
gamma = np.arccos((trace - 1)/2)
scale = np.array([R[2,1] - R[1,2], R[0,2] - R[2,0], R[1,0] - R[0,1]])/(2*np.sin(gamma))

#make the angular velocity
gamma_deg = np.degrees(gamma)
w = np.min(omega_max/scale)
T = abs(gamma/w)

wx = scale[0]*w
wy = scale[1]*w
wz = scale[2]*w


#make the time
t = np.linspace(0, T, 1000)
#make the trajectory
psi_s = [0]
theta_s = [0]
phi_s = [0]
dt = T/1000
for i in range(999):
    psi_s.append(psi_s[i] + wx*dt)
    theta_s.append(theta_s[i] + wy*dt)
    phi_s.append(phi_s[i] + wz*dt)

#plot the trajectory
plt.plot(t, psi_s, label = "psi")
plt.plot(t, theta_s, label = "theta")
plt.plot(t, phi_s, label = "phi")
plt.plot(t, [wx]*1000, label = "wx")
plt.plot(t, [wy]*1000, label = "wy")
plt.plot(t, [wz]*1000, label = "wz")
plt.xlabel("time")
plt.ylabel("angle")

plt.legend()
plt.show()
