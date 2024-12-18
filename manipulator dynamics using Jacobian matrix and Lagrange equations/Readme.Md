This homework assignment for ENPM662 - Fall 2022 focuses on manipulator dynamics, specifically calculating joint torques for a robot's end-effector to draw a circle while compensating for the robot's weight and applying a force. ​ The task involves using the Jacobian matrix and Lagrange equations, with specific assumptions and requirements for the deliverables. ​
Homework Overview

Calculate joint torques for a robot's end-effector to draw a circle. ​
Compensate for the robot's weight and apply a 5N force. ​
Use the Jacobian matrix and Lagrange equations. ​
Assume quasi-static motion (q_dot ≅ 0, q_ddot ≅ 0). ​

Deliverables

PDF report with:

Updated circular trajectory equations for 200 seconds. ​
Explanation of steps and equations for joint torque computation. ​
Mention of used masses and lengths of robot links with citations. ​
Plot of joint torques for joints 1, 2, 4, 5, 6, and 7 from t=0 to t=200 seconds. ​
 ​

Question 1.1:
Given the configurationsof a  PUMA robot, we ened to find DH params, DH diagram and a code to represent reansformation matrix per joint 
N given to be as 200 seconds
Using Euler Lagrangian equations, we need to find gravity matrix 
We need to find the trajectory of joint torques the robot using Euler Lagrangian Equations
Outout of all transformation matrices are givren as screesnshorts , please do check in output folder
Name  of file mano_HW5report.Pdf
Outputs at : Output folder
Code at : Code folder



All codes used:

Codes must print the parametric Gravity matrix gq to the terminal. ​
Codes must plot computed joint torques for all 6 joints. ​
Include a readme file in Markdown format. ​


Submit in a .zip file named _hw5.zip with the following structure:

readme.md
_hw5_report.pdf ​
code (containing all .py files used). ​



Supplementary Material

Robot Dynamics Equation and Lagrangian Dynamics. ​
Kinetic Energy (K) and Potential Energy (P) of the system. ​





