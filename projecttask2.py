#! /usr/bin/env python

# Make a python node executable
# chmod u+x ~/catkin_ws/src/beginner_msgsrv/src/projecttask2.py

import rospy
import sys
from geometry_msgs.msg import Point, Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import pow, atan2, sqrt
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from beginner_msgsrv.srv import*

poseX = 0
poseY = 0
theta = 0

goalpos = Point()
#first way
goalpos.x = int(sys.argv[2])
goalpos.y = int(sys.argv[3])

#second way
#if int(sys.argv[1])==0:
#	goalpos.x=rospy.get_param('goalX_r1')
#	goalpos.y=rospy.get_param('goalY_r1')

#else: 
#	goalpos.x=rospy.get_param('goalX_r2')
#	goalpos.y=rospy.get_param('goalY_r2')

#third way
#if int(sys.argv[1])==0:
#	goalX_r1=-3.0
#	goalY_r1=6.0
#	goalpos.x=goalX_r1
#	goalpos.y=goalY_r1
#else: 
#	goalX_r2=-2.0
#	goalY_r2=4.0
#	goalpos.x=goalX_r2
#	goalpos.y=goalY_r2

def callback(msg):
	global poseX
	global poseY
	global theta

	poseX = msg.pose.pose.position.x
	poseY = msg.pose.pose.position.y

	orientation = msg.pose.pose.orientation
	(roll, pitch, theta) = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])

nodeid = str(sys.argv[1])
nodename = 'robot_' + nodeid
rospy.init_node(nodename, anonymous=True)
pub = rospy.Publisher(nodename + '/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber(nodename + '/odom', Odometry, callback)
rate = rospy.Rate(10)

def euclidean_distance(goal_pose):
	
	global poseX
	global poseY
	rospy.wait_for_service("euclideanDistance")
	try:
		e_dist = rospy.ServiceProxy("euclideanDistance", EuclideanDistance)
		response = e_dist(goal_pose.x, poseX, goal_pose.y, poseY)
		return response.result
	except:
		print("Failed to call service EuclideanDistance")

def linear_vel(goal_pose, constant=1.5):
	return constant * euclidean_distance(goal_pose)

def steering_angle(goal_pose):
	global poseX
	global poseY
	return atan2(goal_pose.y - poseY, goal_pose.x - poseX)

def angular_vel(goal_pose, constant=6):
	global theta
	return constant * (steering_angle(goal_pose) - theta)

def move2goal(goalpos):
	tolerance = 0.01
	vel_msg = Twist()
	while(euclidean_distance(goalpos) >= tolerance):
		vel_msg.linear.x = linear_vel(goalpos)
		vel_msg.linear.y = 0.0
		vel_msg.linear.z = 0.0

		vel_msg.angular.x = 0.0
		vel_msg.angular.y = 0.0
		vel_msg.angular.z = angular_vel(goalpos)

		pub.publish(vel_msg)

	vel_msg.linear.x = 0.0
	vel_msg.angular.z = 0.0
	pub.publish(vel_msg)

	rospy.spin()

move2goal(goalpos)
