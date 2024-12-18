import numpy as np


def calc_area(pose, location):
    #calculate the area of the ellipse as shown above
    phi, theta, psi = pose
    x, y, z = location

    H = np.array([[np.cos(psi)*np.cos(theta), np.cos(psi)*np.sin(theta)*np.sin(phi) - np.sin(psi)*np.cos(phi), np.cos(psi)*np.sin(theta)*np.cos(phi) + np.sin(psi)*np.sin(phi), x],
                    [np.sin(psi)*np.cos(theta), np.sin(psi)*np.sin(theta)*np.sin(phi) + np.cos(psi)*np.cos(phi), np.sin(psi)*np.sin(theta)*np.cos(phi) - np.cos(psi)*np.sin(phi), y],
                    [-np.sin(theta), np.cos(theta)*np.sin(phi), np.cos(theta)*np.cos(phi), z],
                    [0, 0, 0, 1]])
    
    a = H[0,0]*H[0,0] + H[1,0]*H[1,0] - H[2,0]*H[2,0]
    b = 2*(H[0,0]*H[0,1] + H[1,0]*H[1,1] - H[2,0]*H[2,1])
    c = H[0,1]*H[0,1] + H[1,1]*H[1,1] - H[2,1]*H[2,1]
    d = 2*(H[0,0]*H[0,3] + H[1,0]*H[1,3] - H[2,0]*H[2,3])
    e = 2*(H[0,1]*H[0,3] + H[1,1]*H[1,3] - H[2,1]*H[2,3])
    f = H[0,3]*H[0,3] + H[1,3]*H[1,3] - H[2,3]*H[2,3]
   
    det = np.linalg.det([[a, b, d], 
                         [b, c, e], 
                         [d, e, f]])

    area = -np.pi/(a*c - b*2)*(3/2) * det
  
    return area

#take the pose and location as input
pose = input("give pose as phi,theta,psi: ")
location = input("give location as x,y,z: ")
pose = [float(pose) for pose in pose.split(',')]
location = [float(location) for location in location.split(',')]
area = calc_area(pose, location)
print("area: ", area)