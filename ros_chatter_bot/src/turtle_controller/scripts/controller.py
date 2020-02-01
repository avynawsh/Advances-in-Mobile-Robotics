#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def control_loop():
    pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
    rospy.init_node('turtlebot_controller')
    rate = rospy.Rate(1) 
    velocity_msg = Twist()
    velocity_msg.linear.x = 0.3
    velocity_msg.angular.z = 0.2
    while not rospy.is_shutdown():
        pub.publish(velocity_msg)
        print("Controller message pushed at {}".format(rospy.get_time()))
        rate.sleep()

if __name__ == '__main__':
    try:
        control_loop()
    except rospy.ROSInterruptException:
        pass
