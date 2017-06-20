#!/usr/bin/env python
"""
Create a new python script "simple_trajectory_publisher.py". Write code to publish a pre-defined trajectory.

Start with a list of "via points". 
Each time publish a via point (x, y, theta). 
Publish the next point when the current goal is reached.
Use either "Float32MultiArray" or "Pose2D" as the message type.
Publish to topic "robot_controller/pose_goal".
"""
# license removed for brevity
import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Bool
import numpy as np

class trajec_publisher:
    def __init__(self):
        self.pub = rospy.Publisher('robot_controller/pose_goal', Pose2D, queue_size=10)
        rospy.Subscriber('/robot_controller/goal_reached',Bool,self.callback)
        rospy.init_node('talker', anonymous=True)
        self.rate = rospy.Rate(10) # 10hz

        self.achieved_goal = False
        start = Pose2D()
        start.x = 1
        start.y = 0
        start.theta = 0
        self.via_points = [start]
        self.via_index = 0
        next_goal = Pose2D()

        for i in xrange(10):  # move in a straight, horizontal line
            next_goal.x = i+2
            next_goal.y = 0
            next_goal.theta = 0
            self.via_points.append(next_goal)

        self.total_points = len(self.via_points)

    def callback(self,data):
        self.achieved_goal = data
        rospy.loginfo(rospy.get_caller_id() + "I heard" + str(data))

    def talker(self):
        #create a listener for the "goal achieved" message
        #once it hears that bool, it publishes the next message/goal

        while not rospy.is_shutdown():
            if self.achieved_goal:
                self.via_index += 1
            if self.via_index < self.total_points: # off by one errors?
                print("the array is size %d", len(self.via_points))
                print("\taccessing at index %d", self.via_index)
                next_goal = self.via_points[self.via_index] ## Error!! check the logic
                rospy.loginfo(next_goal)
                self.pub.publish(next_goal)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        publisher = trajec_publisher()
        publisher.talker()
    except rospy.ROSInterruptException:
        pass
