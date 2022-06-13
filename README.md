# ROS: Move to Goal 
 
The goal in this task is to move the robot to a goal point in ROS Stage and Gazebo (with Turtlebot3 Burger robots).
The goal points will be determined in 3 ways and each way should be separately tested.

1. Way-1: Create a launch file named “task2launch1.launch” that includes the robots’ goal point parameters
(goalX_r1 (float), goalY_r1(float), goalX _r2 (float), and goalY_r2(float)), also runs ROS Stage and
“projecttask2.py” node for both robots. The code should send the first robot to the goal point (goalX_r1,
goalY_r1), and the second robot to the goal point (goalX_r2, goalY_r2).

2. Way-2: Create a launch file named “task2launch2.launch” that recevies the goal point parameters from a
YAML file and runs ROS Stage and the “projecttask2.py” node for both robots. The YAML file will include
the parameters goalX_r1 (float), goalY_r1(float), goalX _r2 (float), and goalY_r2(float). The code should
send the first robot to the goal point (goalX_r1, goalY_r1), and the second robot to the goal point
(goalX_r2, goalY_r2).

3. Way-3: Create a launch file named “task2launch3.launch” that only runs the “projecttask2.py” node for
both robots. In way-3, give fixed goal point values in “projecttask2.py” node. For example: goalX_r1 = 2,
goalY_r1 =2, goalX_r2 = 4, and goalY_r2 =4.

In the code “projecttask2.py” created a service (called “distanceservice.py” in Python) that does the job of the “euclidean_distance” function. The service requires 4 floating point parameters representing the coordinates of two points and returns the euclidean distance between those points. Called this service in node's euclidean_distance function to calculate the euclidean distance between the robot's current position and target position. Instead of using the "return sqrt(...)" line in the euclidean_distance function, now call your new service in this function and the result the service provided is returned.
