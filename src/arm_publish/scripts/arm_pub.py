#! /usr/bin/env python

import rospy
from std_msgs.msg import Float64

class arm_joint_publisher:
    def __init__(self,name):
        self.pub = rospy.Publisher(name,Float64,queue_size=10)
        self.theta = 0
        self.direction = True
    def publish(self):
        self.pub.publish(self.theta)
    def set_theta(self,theta):
        self.theta = theta

if __name__ == "__main__":
 
    rospy.init_node("talker_p")
    c1 = "mycar/joint1_controller/command"
    c2 = "mycar/joint2_controller/command"
    c3 = "mycar/joint3_controller/command"
    c4 = "mycar/joint4_controller/command"
    c5 = "mycar/joint5_controller/command"
    c6 = "mycar/joint6_controller/command"
    pub1 = arm_joint_publisher(c1)
    pub2 = arm_joint_publisher(c2)
    pub3 = arm_joint_publisher(c3)
    pub4 = arm_joint_publisher(c4)
    pub5 = arm_joint_publisher(c5)
    pub6 = arm_joint_publisher(c6)
    theta1 = 0.0  
    theta2 = 0.0
    theta3 = 0.0
    theta4 = 0.0
    theta5 = 0.0
    theta6 = 0.0
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        pub1.set_theta(theta1)
        pub2.set_theta(theta2)
        pub3.set_theta(theta3)
        pub4.set_theta(theta4)
        pub5.set_theta(theta5)
        pub6.set_theta(theta6)
        pub1.publish()
        pub2.publish()
        pub3.publish()
        pub4.publish()
        pub5.publish()
        pub6.publish()
        rate.sleep()
        #rospy.loginfo("output_theta1:%s",theta1)
        
        theta1 += 0.04
        
        if pub2.direction:
            theta2 += 0.02
        else:
            theta2 -= 0.02
       
        if pub3.direction:
            theta3 += 0.02
        else:
            theta3 -= 0.02
        theta4 += 0.02
        ''''''
        if pub5.direction:
            theta5 += 0.015
        else:
            theta5 -= 0.015
        
        if theta2 > 0.1:
            pub2.direction = False
        if theta2 < -0.78:
            pub2.direction = True
        
        if theta1 > 3.14:
            theta1 = -3.14
        
        if theta3 > 0.78:
            pub3.direction = False
        if theta3 < -0.78:
            pub3.direction = True
        if theta4 > 3.14:
            theta4 = -3.14

        if theta5 > 0.3:
            pub5.direction = False
        if theta5 < -0.3:
            pub5.direction = True
        '''    
        if theta6 > 3.14:
            theta6 = -3.14
        '''