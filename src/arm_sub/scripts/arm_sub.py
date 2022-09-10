#! /usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import WrenchStamped
from std_msgs.msg import Float64

class filter:
    def __init__(self,size):
        self.filter_size = size
        self.nums = np.zeros(self.filter_size)
        self.size = 0
        self.sum = 0
    def compute(self, input):
        if self.size < self.filter_size:
            self.nums[self.size] = input
            self.size = self.size + 1
            self.sum = self.sum + input
            return self.sum/self.size
        if self.size == self.filter_size:
            tmp = self.nums[0]
            for i in range(self.filter_size - 1):
                self.nums[i] = self.nums[i + 1]
            self.nums[self.filter_size - 1] = input
            self.sum = self.sum + input - tmp
            return self.sum/self.filter_size

jf1 = filter(10)
jf2 = filter(20)
jf3 = filter(20)
jf4 = filter(10)
jf5 = filter(10)
jf6 = filter(10)

pub11 = rospy.Publisher('joint_1',Float64,queue_size=10)
pub22 = rospy.Publisher('joint_2',Float64,queue_size=10)
pub33 = rospy.Publisher('joint_3',Float64,queue_size=10)
pub44 = rospy.Publisher('joint_4',Float64,queue_size=10)
pub55 = rospy.Publisher('joint_5',Float64,queue_size=10)
pub66 = rospy.Publisher('joint_6',Float64,queue_size=10)

def doMsg1(msg):
    #rospy.loginfo("I heard from 1:%s",msg.wrench.torque.z)
    if abs(msg.wrench.torque.z) < 100:
        res1 = jf1.compute(msg.wrench.torque.z)
        pub11.publish(res1)
def doMsg2(msg):
    #rospy.loginfo("I heard from 2:%s",msg.wrench)
    if abs(msg.wrench.torque.z) < 100:
        res2 = jf2.compute(msg.wrench.torque.z)
        pub22.publish(res2)
def doMsg3(msg):
    #rospy.loginfo("I heard from 3:%s",msg.wrench)
    if abs(msg.wrench.torque.z) < 100:
        res3 = jf3.compute(msg.wrench.torque.z)
        pub33.publish(res3)
def doMsg4(msg):
    #rospy.loginfo("I heard from 4:%s",msg.wrench)
    if abs(msg.wrench.torque.z) < 100:
        res4 = jf4.compute(msg.wrench.torque.z)
        pub44.publish(res4)
def doMsg5(msg):
    #rospy.loginfo("I heard from 5:%s",msg.wrench)
    if abs(msg.wrench.torque.z) < 100:
        res5 = jf5.compute(msg.wrench.torque.z)
        pub55.publish(res5)
def doMsg6(msg):
    #rospy.loginfo("I heard from 6:%s",msg.wrench)
    if abs(msg.wrench.torque.z) < 100:
        res6 = jf6.compute(msg.wrench.torque.z)
        pub66.publish(res6)

if __name__ == "__main__":
    rospy.init_node("listener")
    sub1 = rospy.Subscriber("ftsensor1_topic",WrenchStamped,doMsg1,queue_size=10)
    sub2 = rospy.Subscriber("ftsensor2_topic",WrenchStamped,doMsg2,queue_size=10)
    sub3 = rospy.Subscriber("ftsensor3_topic",WrenchStamped,doMsg3,queue_size=10)
    sub4 = rospy.Subscriber("ftsensor4_topic",WrenchStamped,doMsg4,queue_size=10)
    sub5 = rospy.Subscriber("ftsensor5_topic",WrenchStamped,doMsg5,queue_size=10)
    sub6 = rospy.Subscriber("ftsensor6_topic",WrenchStamped,doMsg6,queue_size=10)

    rospy.spin()