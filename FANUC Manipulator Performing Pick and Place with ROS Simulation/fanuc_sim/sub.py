#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def joint1_callback(data):
    rospy.loginfo("Received joint1 command: %s", data.data)

def joint2_callback(data):
    rospy.loginfo("Received joint2 command: %s", data.data)

def joint3_callback(data):
    rospy.loginfo("Received joint3 command: %s", data.data)

def joint4_callback(data):
    rospy.loginfo("Received joint4 command: %s", data.data)

def joint5_callback(data):
    rospy.loginfo("Received joint5 command: %s", data.data)

def joint6_callback(data):
    rospy.loginfo("Received joint6 command: %s", data.data)

def gripper_callback(data):
    rospy.loginfo("Received gripper command: %s", data.data)

if __name__ == '__main__':
    rospy.init_node('fanuc_sim_subscriber', anonymous=True)

    rospy.Subscriber('fanuc_sim/link_1_motor/command', Float64, joint1_callback)
    rospy.Subscriber('fanuc_sim/link_2_motor/command', Float64, joint2_callback)
    rospy.Subscriber('fanuc_sim/link_3_motor/command', Float64, joint3_callback)
    rospy.Subscriber('fanuc_sim/link_4_motor/command', Float64, joint4_callback)
    rospy.Subscriber('fanuc_sim/link_5_motor/command', Float64, joint5_callback)
    rospy.Subscriber('fanuc_sim/link_6_motor/command', Float64, joint6_callback)
    rospy.Subscriber('fanuc_sim/gripper/command', Float64, gripper_callback)

    rospy.spin()
