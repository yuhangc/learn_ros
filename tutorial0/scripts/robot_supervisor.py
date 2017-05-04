#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Bool
from kobuki_msgs.msg import BumperEvent

import numpy as np


class RobotSupervisor:
    def __init__(self):
        # subscribers
        rospy.Subscriber("mobile_base/events/bumper", BumperEvent, self.bumper_event_callback)
        rospy.Subscriber("robot_controller/goal_reached", Bool, self.goal_reached_callback)

        # publishers
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
        self.enable_controller_pub = rospy.Publisher('/robot_controller/enable_controller', Bool, queue_size=10)

        # TODO: initialize any parameters for your controller

        # pose_goal is the target pose of the robot
        self.pose_goal = Pose2D()
        self.pose_goal.x = rospy.get_param("~pose_goal_x", 5.0)
        self.pose_goal.y = rospy.get_param("~pose_goal_y", 5.0)
        self.pose_goal.theta = rospy.get_param("~pose_goal_theta", 0.0)

        # bumper event records which bumper is pressed
        # example usage:
        # if self.bumper_event.state == BumperEvent.PRESSED:
        #     do something
        # if self.bumper_event.bumper == BumperEvent.LEFT:
        #     do something
        self.bumper_event = BumperEvent()

        # indicates whether the current via point is reached
        self.flag_viapoint_reached = False

        # valid states
        # TODO: add in or change the valid state based on your design of the state machine
        self.valid_states = ["idle", "moving_to_next", "backing_up", "exploring_boundary", "goal_reached"]

        # set the initial state
        self.state = "idle"

    def bumper_event_callback(self, bumper_msg):
        self.bumper_event = bumper_msg

    def goal_reached_callback(self, goal_reached_msg):
        if goal_reached_msg.data:
            self.flag_viapoint_reached = True

    def state_machine(self):
        # the state has to be valid
        if self.state not in self.valid_states:
            rospy.logerr("Invalid state!")
            return

        # TODO: complete the state machine
        # note that python doesn't have switch-case statement
        if self.state == "idle":
            pass
        elif self.state == "moving_to_next":
            pass
        elif self.state == "backing_up":
            pass
        elif self.state == "exploring_boundary":
            pass
        elif self.state == "goal_reached":
            pass

    def run(self):
        rospy.init_node('turtlebot_supervisor')

        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            self.state_machine()
            rate.sleep()


if __name__ == "__main__":
    supervisor = RobotSupervisor()
    supervisor.run()
