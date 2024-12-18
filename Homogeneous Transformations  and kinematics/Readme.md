Homework 2 for ENPM662 Introduction to Robot Modeling. ​ 
1 Homogeneous Transformations ​
1.1 Composition of transforms ​

Sequence of transformations: rotate by ϕ about the world x-axis, translate by y along the current y-axis, rotate by θ about the world z-axis, and rotate by ψ about the current x-axis. ​
Write the matrix production equation using rotation matrices Rangle and translation matrices Tdistance to get the resulting pose of the frame. ​

1.2 Modeling beyond rigid transformations ​

Consider a camera rigidly mounted on a drone hovering over a plane with a view modeled as a cone with an apex angle α = 45°. ​
Derive the expression for the coverage area in terms of three consecutive rotations ψ, θ, ϕ, and 3D location dx, dy, dz relative to the world frame on the ground plane. ​
Write a Python function that takes these six inputs and outputs the area. ​

1.3 Transform Estimation ​

Derive the expression for the transformation matrix H from frame to ′, considering the location of point P relative to frames ′ and assuming the frame is only rotated about the Z-axis with angle ϕ and translated freely in 3D space. ​

2 Kinematics
2.1 Trajectory Optimisation ​

The drone moves from position X, Y, Z to X’, Y’, Z’ with final orientation ψg = 35°, θg = 15°, ϕg = 20° and ωmax = 1deg/s. ​
Plot the trajectory of the drone to reach the final orientation in the shortest time, representing the trajectory plots of ψ, θ, ϕ, ωx, ωy, ωz with respect to time. ​
Describe computations in the report. ​
Assumptions: position X, Y, Z is aligned with the global frame, ψ, θ, ϕ are consecutive rotations about global X, Y, Z axes, ωx, ωy, ωz are angular velocities about the drone’s local X, Y, Z axes, and angular velocities can be changed arbitrarily within the limit ​ |ωx|, |ωy|, |ωz| ≤ ωmax.

3 Appendix

Re-write equations in homogeneous matrix multiplication form. ​
The area of an ellipse given by the equation ax² + 2bxy + cy² + 2dx + 2ey + f = 0 is A = −π (ac − b²)^(3/2) / (b d b c e d e f). ​
