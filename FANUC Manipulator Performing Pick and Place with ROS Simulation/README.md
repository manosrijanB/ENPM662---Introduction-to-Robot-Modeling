
FANUC Manipulator Simulation

Overview
This project simulates the FANUC manipulator performing pick-and-place tasks using ROS (Robot Operating System) in Gazebo and RVIZ environments. The project includes modeling, kinematics (both forward and inverse), and control for the FANUC manipulator.

 Files

 To Run:
- Teleoperation Launch:  
  To launch the teleoperation for the manipulator, run:  
  ```bash
  roslaunch fanuc_sim teleop_manipulator.launch
  ```

- Publisher Script:  
  To run the publisher for communication, execute:  
  ```bash
  python3 pub.py
  ```

- Main Launch Files:  
  To start the full FANUC simulation, use:  
  ```bash
  roslaunch fanuc_sim full_fanuc_sim.launch
  ```

- Inverse Kinematics:  
  To compute the inverse kinematics and generate trajectories, run:  
  ```bash
  python3 invk.py
  ```

- Forward Kinematics:  
  To compute forward kinematics, execute:  
  ```bash
  python3 fwk.py
  ```

CAD Files:
The project includes CAD files that consist of the important assembly files and part files for the FANUC manipulator.

Requirements:
- ROS (Robot Operating System)
- Gazebo
- RVIZ
- Python 3
- Required ROS packages for FANUC manipulator simulation

 Conclusion:
This simulation provides insights into the FANUC manipulator's functionality and its applications in industrial automation tasks, including pick-and-place operations. Future work will involve improvements in controller interactions and task execution.
