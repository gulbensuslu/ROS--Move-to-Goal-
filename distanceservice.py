#!/usr/bin/env python
# chmod u+x catkin_ws/src/beginner_msgsrv/src/distanceservice.py

import rospy
from math import pow,sqrt
from beginner_msgsrv.srv import EuclideanDistance, EuclideanDistanceResponse
        
def euclidean_distance(req):
	
	return EuclideanDistanceResponse(sqrt(pow((req.goal_poseX-req.self_poseX),2.0)+pow(( req.goal_poseY-req.self_poseY),2.0)))
	
def movetogoalServer():
	print("Ready to move to goal.")
	rospy.init_node("euclidean_distance_server")
	rospy.Service('euclideanDistance', EuclideanDistance, euclidean_distance)
	rospy.spin()

if __name__ == "__main__":
	movetogoalServer()
