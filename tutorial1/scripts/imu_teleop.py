#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray


class ImuTeleop:
    def __init__(self):
        # desired velocity for publish
        self.cmd_vel = Twist()

        # variables for tilt control
        self.roll_to_linear_scale = rospy.get_param("~roll_to_linear_scale", -1.0)
        self.pitch_to_angular_scale = rospy.get_param("~pitch_to_angular_scale", -2.0)
        self.pitch_deadband = rospy.get_param("~pitch_deadband", 0.2)
        self.roll_deadband = rospy.get_param("~roll_deadband", 0.2)
        self.pitch_offset = rospy.get_param("~pitch_offset", 0.15)
        self.roll_offset = rospy.get_param("~roll_offset", 0.1)

        # TODO: subscribers to IMU data
        self.human_input_ort_sub = None

        # publisher to robot velocity
        self.robot_vel_pub = rospy.Publisher("/cmd_vel",
                                             Twist, queue_size=1)

    # TODO: define callback functions

    # utility functions
    def send_vel_cmd(self, vx, omg):
        # set and send desired velocity
        self.cmd_vel.linear.x = vx
        self.cmd_vel.angular.z = omg

        self.robot_vel_pub.publish(self.cmd_vel)

    # convert euler angles from IMU data
    def euler_from_imu(self):
        roll, pitch, yaw = (0.0, 0.0, 0.0)
        # TODO: convert imu data into euler angles
        return roll, pitch, yaw

    # main teleoperation function
    def calculate_control(self):
        roll, pitch, yaw = self.euler_from_imu()

        # TODO: calculate desired velocities based on pitch and roll angles
        vx, om = (0.0, 0.0)
        if pitch > self.roll_deadband:
            pass
        elif pitch < -self.roll_deadband:
            pass

        if roll > self.pitch_deadband:
            pass
        elif roll < -self.pitch_deadband:
            pass

        self.send_vel_cmd(vx, om)


if __name__ == "__main__":
    # initialize node
    rospy.init_node("teleop")

    # create a teleop object
    teleop = ImuTeleop()

    # loop rate 50 Hz
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        teleop.calculate_control()
        rate.sleep()
