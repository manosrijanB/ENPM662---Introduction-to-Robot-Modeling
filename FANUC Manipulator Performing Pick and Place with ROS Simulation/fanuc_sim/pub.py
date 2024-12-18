#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import sys, select, termios, tty

class TeleopNode(object):
    def __init__(self):
        self.msg = """
        Control Your RDSS!
        ---------------------------
        Manipulator keys:
           Joint 1: 1,q
           Joint 2: 2,w
           Joint 3: 3,e
           Joint 4: 4,r
           Joint 5: 6,y
           Joint 6: 7,8
           s,x : open and close hand
        """

        self.moveBindings = {
            'i':(1,0),
            'o':(1,-1),
            'j':(0,1),
            'l':(0,-1),
            'u':(1,1),
            ',':(-1,0),
            '.':(-1,1),
            'm':(-1,-1),
        }

        self.speedBindings={
            'q':(1.1,1.1),
            'z':(.9,.9),
            'w':(1.1,1),
            'x':(.9,1),
            'e':(1,1.1),
            'c':(1,.9),
        }

        self.speed = 8
        self.turn = 0.5

        self.joint_publishers = [
            rospy.Publisher('fanuc_sim/link_1_motor/command', Float64, queue_size=10),
            rospy.Publisher('fanuc_sim/link_2_motor/command', Float64, queue_size=10),
            rospy.Publisher('fanuc_sim/link_3_motor/command', Float64, queue_size=10),
            rospy.Publisher('fanuc_sim/link_4_motor/command', Float64, queue_size=10),
            rospy.Publisher('fanuc_sim/link_5_motor/command', Float64, queue_size=10),
            rospy.Publisher('fanuc_sim/link_6_motor/command', Float64, queue_size=10),
            rospy.Publisher('fanuc_sim/gripper/command', Float64, queue_size=10)
        ]

        self.settings = termios.tcgetattr(sys.stdin)

    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def vels(self):
        return "currently:\tspeed %s\tturn %s " % (self.speed,self.turn)

    def clamp(self, x, min_val, max_val):
        return max(min(x, max_val), min_val)

    def run(self):
        rospy.init_node('teleop_node')
        rate = rospy.Rate(10)  # 10 Hz

        x = 0
        y = 0
        z = 0
        th = 0
        gripper = 0

        try:
            print(self.msg)
            print(self.vels())
            while not rospy.is_shutdown():
                key = self.getKey()
                if key in self.moveBindings.keys():
                    x += self.moveBindings[key][0] * self.speed
                    y += self.moveBindings[key][1] * self.speed
                    z = self.clamp(z, -1.57, 1.57)
                    th = self.clamp(th, -1.57, 1.57)
                    self.joint_publishers[0].publish(Float64(x))
                    self.joint_publishers[1].publish(Float64(y))
                    self.joint_publishers[2].publish(Float64(z))
                    self.joint_publishers[3].publish(Float64(th))
                elif key in self.speedBindings.keys():
                    self.speed = self.speed * self.speedBindings[key][0]
                    self.turn = self.turn * self.speedBindings[key][1]

                    print(self.vels())
                    if (self.speed > 10):
                        self.speed = 10
                    elif (self.speed < 1):
                        self.speed = 1

                elif key == 's':
                    gripper = 0.0
                    self.joint_publishers[6].publish(Float64(gripper))

                elif key == 'x':
                    gripper = 0.7
                    self.joint_publishers[6].publish(Float64(gripper))

                elif key == ' ':
                    x = 0
                    y = 0
                    z = 0
                    th = 0
                    gripper = 0
                    self.joint_publishers[0].publish(Float64(x))
                    self.joint_publishers[1].publish(Float64(y))
                    self.joint_publishers[2].publish(Float64(z))
                    self.joint_publishers[3].publish(Float64(th))
                    self.joint_publishers[6].publish(Float64(gripper))

                else:
                    if (key == '\x03'):
                        break

                rate.sleep()

        finally:
            self.joint_publishers[0].publish(Float64(0))
            self.joint_publishers[1].publish(Float64(0))
            self.joint_publishers[2].publish(Float64(0))
            self.joint_publishers[3].publish(Float64(0))
            self.joint_publishers[4].publish(Float64(0))
            self.joint_publishers[5].publish(Float64(0))
            self.joint_publishers[6].publish(Float64(0))

            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)

