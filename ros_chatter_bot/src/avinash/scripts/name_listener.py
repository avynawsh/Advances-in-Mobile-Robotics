#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String

def talker(greeting):
    pub = rospy.Publisher('chatter_name',String,queue_size=10)  #publishing to chatter node
    rospy.init_node('name_listener', anonymous = True)
    rate= rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = greeting
        # rospy.loginfo(msg)       # ros py printing function
        pub.publish(msg)         #Publishing the message to chatter node
        rate.sleep()


if __name__ == "__main__":
    try:
        talker(sys.argv[1])
    except rospy.ROSInterruptException:
        pass

