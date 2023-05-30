#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty, EmptyResponse

def home_trigger():
    rospy.wait_for_service('/go_home')
    try:
        trigger = rospy.ServiceProxy('/go_home', Empty)
        print("Please do something.")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed to home: %s"%e)

def kitchen_trigger():
    rospy.wait_for_service('/go_to_kitchen')
    try:
        trigger = rospy.ServiceProxy('/go_to_kitchen', Empty)
        print("Please do something.")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed to kitchen: %s"%e)

def stop_trigger():
    rospy.wait_for_service('/stop')
    try:
        trigger = rospy.ServiceProxy('/stop', Empty)
        print("Please do something.")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed to stop: %s"%e)


if __name__ == '__main__':
    kitchen_trigger()
    stop_trigger()
    home_trigger()
    stop_trigger()