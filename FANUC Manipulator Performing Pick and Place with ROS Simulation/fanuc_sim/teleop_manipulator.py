#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import sys, select, termios, tty

msg = """
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

moveBindings = {
    'i':(1,0),
    'o':(1,-1),
    'j':(0,1),
    'l':(0,-1),
    'u':(1,1),
    ',':(-1,0),
    '.':(-1,1),
    'm':(-1,-1),
}

speedBindings={
    'q':(1.1,1.1),
    'z':(.9,.9),
    'w':(1.1,1),
    'x':(.9,1),
    'e':(1,1.1),
    'c':(1,.9),
}

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 8
turn = 0.5

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

def clamp(x, min_val, max_val):
    return max(min(x, max_val), min_val)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('turtlebot_teleop')

    pub_j1 = rospy.Publisher('fanuc_sim/link_1_motor/command', Float64, queue_size=10)
    pub_j2 = rospy.Publisher('fanuc_sim/link_2_motor/command', Float64, queue_size=10)
    pub_j3 = rospy.Publisher('fanuc_sim/link_3_motor/command', Float64, queue_size=10)
    pub_j4 = rospy.Publisher('fanuc_sim/link_4_motor/command', Float64, queue_size=10)
    pub_j5 = rospy.Publisher('fanuc_sim/link_5_motor/command', Float64, queue_size=10)
    pub_j6 = rospy.Publisher('fanuc_sim/link_6_motor/command', Float64, queue_size=10)
    pub_j6 = rospy.Publisher('fanuc_sim/link_6_motor/command', Float64, queue_size=10)
    pub_hand = rospy.Publisher('fanuc_sim/gripper/command', Float64, queue_size=10)
    speed = rospy.get_param("~speed", 8)
turn = rospy.get_param("~turn", 0.5)

x = 0
y = 0
z = 0
th = 0
gripper = 0

try:
    print(msg)
    print(vels(speed,turn))
    while(1):
        key = getKey()
        if key in moveBindings.keys():
            x += moveBindings[key][0] * speed
            y += moveBindings[key][1] * speed
            z = clamp(z, -1.57, 1.57)
            th = clamp(th, -1.57, 1.57)
        elif key in speedBindings.keys():
            speed *= speedBindings[key][0]
            turn *= speedBindings[key][1]

            print(vels(speed,turn))
            if (status == 14):
                print(msg)
            status = (status + 1) % 15
        elif key == 's':
            gripper = 0.03
        elif key == 'x':
            gripper = -0.03

        if key in ['1', 'q']:
            pub_j1.publish(th)
        elif key in ['2', 'w']:
            pub_j2.publish(th)
        elif key in ['3', 'e']:
            pub_j3.publish(th)
        elif key in ['4', 'r']:
            pub_j4.publish(th)
        elif key in ['6', 'y']:
            pub_j5.publish(th)
        elif key in ['7', '8']:
            pub_j6.publish(th)
        elif key == 's' or key == 'x':
            pub_hand.publish(gripper)

        th = clamp(th, -1.57, 1.57)

except Exception as e:
    print(e)

finally:
    pub_j1.publish(0)
    pub_j2.publish(0)
    pub_j3.publish(0)
    pub_j4.publish(0)
    pub_j5.publish(0)
    pub_j6.publish(0)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)





