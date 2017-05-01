#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Bool

import tf

import numpy as np


class RobotController:
    def __init__(self):
        rospy.Subscriber('/gazebo/model_states', ModelStates, self.robot_state_callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
        self.goal_reached_pub = rospy.Publisher('/robot_controller/goal_reached', Bool, queue_size=10)

        # TODO: initialize any parameters for your controller

        # (x, y, theta) is the pose of the robot
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # pose_goal is the target pose of the robot
        self.pose_goal = Pose2D()

    def robot_state_callback(self, state_msg):
        """
        Get pose from the message data
        """
        pose = state_msg.pose[state_msg.name.index("mobile_base")]
        twist = state_msg.twist[state_msg.name.index("mobile_base")]
        self.x = pose.position.x
        self.y = pose.position.y
        quaternion = (
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z,
            pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        self.theta = euler[2]

    def calc_control(self, pose_goal):
        """
        Calculate the closed-loop control for tracking the target pose
        :param pose_goal: Pose2D type, the target pose
        :return: Return control (Twist) or None if goal is reached
        """
        cmd_vel = Twist()

        # TODO: fill in your favorite controller

        return cmd_vel

    def run(self):
        rospy.init_node('turtlebot_controller')

        # TODO: fill in the main run function


if __name__ == "__main__":
    controller = RobotController()
    controller.run()
