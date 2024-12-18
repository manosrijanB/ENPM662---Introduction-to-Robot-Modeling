# README for Homework 1 Submission

## Assignment Overview
This homework focuses on basic robot modeling concepts. It consists of two main parts:

1. **Kinematics of a Rear Wheel Drive Vehicle**
2. **Forward and Inverse Kinematics of a 3-DOF Serial Manipulator**


## Part 1: Rear Wheel Drive Modeling

### Task
- Derive the state-space model for a rear-wheel drive vehicle (nonholonomic model).
- Given:
  - Initial pose \((x_i, y_i, \phi_i)\)
  - Drive speed \(\omega\)
  - Steering angle \(\alpha\)
  - Duration \( T \)
- Parameters:
  - Wheel diameter = 0.5 m
  - Chassis length = 4 m
  - Distance between wheels = 1.5 m
- Condition: The drive speed is distributed between the two wheels such that \(\omega_{\text{left}} + \omega_{\text{right}} = 2\omega\).

### Requirements
1. **Derivation**: Show all steps in your report to derive the kinematic equations and final state-space model.
2. **Implementation**: Write a Python program that:
   - Takes the initial conditions, \(\omega\), \(\alpha\), and \(T\) as inputs.
   - Simulates the motion of the vehicle.
   - Plots the 2D trajectory of the point O (e.g., the midpoint between the two rear wheels).
   
### Running the Code
- Run `python rear_wheel_drive.py`.
- The script will:
  - Compute the trajectory.
  - Generate and display a plot of the vehicle’s path.
  
Ensure you have installed required libraries (e.g., `matplotlib`, `numpy`).

---

## Part 2: Kinematics of a 3-DOF Manipulator

### Task
- Consider a 3-link serial manipulator with revolute joints.  
  Joint angles: \(\theta_1, \theta_2, \theta_3\)  
  Link lengths: \(l_1, l_2, l_3\)
- Derive:
  1. **Forward Kinematics (Position and Velocity)**:  
     Find end-effector position \((x, y, \phi)\) and velocities \((\dot{x}, \dot{y}, \dot{\phi})\) in terms of \(\theta_i\) and \(\dot{\theta}_i\).
  2. **Inverse Velocity Kinematics**:  
     Derive the matrix equation that, given \((\dot{x}, \dot{y}, \dot{\phi})\) and \((\theta_1, \theta_2, \theta_3)\), solves for \((\dot{\theta}_1, \dot{\theta}_2, \dot{\theta}_3)\).
  
  Use Python’s `SymPy` library to automate differentiation where needed.

### Requirements
1. **Derivation**: Show your geometrical derivation steps in the PDF report.
2. **Code Implementation**:
   - Write a Python script (e.g., `manipulator_kinematics.py`).
   - Implement functions for:
     - Forward kinematics (both position and velocity).
     - Inverse velocity kinematics using a matrix inversion approach.
   - Use `SymPy` for symbolic derivation and verification.

### Running the Code
- Run `python manipulator_kinematics.py`.
- The script will:
  - Print out symbolic expressions for forward kinematics and the inverse velocity kinematics matrix.
  - Optionally, you can plug in numerical values of \(\theta_i\) and \(\dot{x}, \dot{y}, \dot{\phi}\) to verify correctness.

---

