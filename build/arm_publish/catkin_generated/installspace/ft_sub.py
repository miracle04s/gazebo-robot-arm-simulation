#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import WrenchStamped

def doMsg(msg):
    rospy.loginfo("I heard:%s",msg.data)

if __name__ == "__main__":
    rospy.init_node("listener")

    sub = rospy.Subscriber("ftsensor2_topic",WrenchStamped,doMsg,queue_size=10)

    rospy.spin()
