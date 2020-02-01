#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String, Int64

global name,roll

# name = ''
# roll = 0
def callback_name(data):
    # print(data.data,type(data.data))
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # print(data.data)
   
    global name
    name = data.data
    #name =str(name)
    # print(name)
    

def callback_roll(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    global roll 
    roll = data.data
    #roll=int(roll)
    # print(roll)
    rospy.loginfo("Student {} has roll number {}".format(name,roll))

def listener():
    # global name, roll
    # name= "a"
    # roll = 1 
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('chatter_name', String, callback_name)
    rospy.Subscriber('chatter_roll', Int64, callback_roll)
    # rospy.loginfo("Student {} has roll number {}".format(name,roll))
    # print(globals())
    # print(d['name'],d['roll'])
    rospy.spin()

listener()
