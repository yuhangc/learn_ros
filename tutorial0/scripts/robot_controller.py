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
        rospy.init_node('turtlebot_controller')

        rospy.Subscriber('/gazebo/model_states', ModelStates, self.robot_state_callback)
        rospy.Subscriber('robot_controller/pose_goal', Pose2D, self.goal_callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
        self.goal_reached_pub = rospy.Publisher('/robot_controller/goal_reached', Bool, queue_size=10)
        self.rate = rospy.Rate(10)

        # TODO: initialize any parameters for your controller
        self.k_x = 10
        self.k_y = .0064
        self.k_theta = 0.16

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
        pose = state_msg.pose[state_msg.name.index("mobile_base")]## Error getting this to work
        twist = state_msg.twist[state_msg.name.index("mobile_base")]

        # pose = state_msg.pose
        # twist = state_msg.twist
        self.x = pose.position.x
        self.y = pose.position.y
        quaternion = (
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z,
            pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        self.theta = euler[2]

    def goal_callback(self, data):
        """
        Get next goal from the message data
        """
        self.pose_goal = data


    def calc_control(self):
        """
        Calculate the closed-loop control for tracking the target pose
        :param pose_goal: Pose2D type, the target pose
        :return: Return control (Twist) or None if goal is reached
        """
        cmd_vel = Twist()

        # TODO: fill in your favorite controller
        # calculate the proximity to the goal
        threshold = 0.1
        if self.pose_goal.x - self.x <= threshold and self.pose_goal.y - self.y <= threshold:
            cmd_vel.linear = 0
            cmd_vel.angular = 0
            self.cmd_vel_pub.publish(cmd_vel)
            return None # close to goal
        else:
            # do control calculations
            theta_e = -self.theta
            x_e = self.pose_goal.x - self.x
            y_e = self.pose_goal.y - self.y
            v_r = 30 #in centimeters.  Check if pose returns meter or cm
            w_r = 0
            cmd_vel.linear = v_r*np.cos(theta_e) + self.k_x*x_e
            cmd_vel.angular = w_r + v_r*(self.k_y*y_e + self.k_theta*np.sin(theta_e))
            return cmd_vel

    def run(self):
        # TODO: fill in the main run function
        while not rospy.is_shutdown():
            response = self.calc_control()
            if(response == None): # publish message "goal reached"
                self.goal_reached_pub.publish(True)
            # else:
                # self.cmd_vel_pub.publish(response) ##Error!! no attribute .x? I think there's a type error somehow
            self.rate.sleep()


if __name__ == "__main__":
    controller = RobotController()
    controller.run()
