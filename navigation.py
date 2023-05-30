#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty,EmptyResponse
import time

t=2

def go_home(req1):
    rospy.loginfo("Going to home")
    time.sleep(t)
    rospy.loginfo("Arrived home")
    return EmptyResponse()

def go_to_kitchen(req):
    rospy.loginfo("Going to kitchen")
    time.sleep(t)
    rospy.loginfo("Arrived kitchen")
    return EmptyResponse()

def stop(req):
    rospy.loginfo("Stop")
    return EmptyResponse()

def main_server():
    rospy.init_node('main_server')
    kitchen = rospy.Service('/go_to_kitchen', Empty, go_to_kitchen)
    print("Ready to do something.")
    home = rospy.Service('/go_home', Empty, go_home)
    print("Ready to do something.")
    Stop_robot = rospy.Service('/stop', Empty, stop)
    print("Ready to do something.")
    rospy.spin()

if __name__ == "__main__":
    main_server()