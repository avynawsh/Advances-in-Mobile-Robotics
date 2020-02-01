#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import Int64

def talker(greeting):
    pub = rospy.Publisher('chatter_roll',Int64,queue_size=10)  #publishing to chatter2 node
    rospy.init_node('roll_listener', anonymous = True)
    rate= rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = int(greeting)
        # rospy.loginfo(msg)       # i think we have to log into ros along with our contents to publish before publish 
        pub.publish(msg)         #Publishing the message to chatter node
        rate.sleep()


if __name__ == "__main__":
    try:
        talker(sys.argv[1])
    except rospy.ROSInterruptException:
        pass

