#include "serial_manager.h"
#include <string>
#include <iostream>
#include <sstream>

// ============================================================================
// constructor
SerialManager::SerialManager(ros::NodeHandle &nh, ros::NodeHandle &pnh) : nh_(nh)
{
    // TODO: initialize publishers (and subscribers/parameters)
    // this->serial_data_pub =

    // initialize the arduino device
    this->arduino = new CArduinoDevice("/dev/ttyACM0",CArduinoDevice::BAUD_115200);
    if (!this->arduino->connect()) {
        ROS_ERROR("Cannot connect to input device!");
    } else {
        ROS_INFO("Input device connected");
    }
}

// ============================================================================
// destructor
SerialManager::~SerialManager()
{
    delete this->arduino;
}

// ============================================================================
// main update
void SerialManager::update()
{
    // check whether the device is still connected
    if (!this->arduino->isConnected()) {
        ROS_WARN("Input device not connected! Try to connect again");
        if (this->arduino->connect()) {
            ROS_INFO("Input device connected");
        } else {
            ROS_ERROR("Cannot connect to input device!");
            return;
        }
    }

    // read message from serial port
    std::string message;
    int read_n = this->arduino->read(message);

    // TODO: process and publish the message
    std::stringstream ss(message);
    if (read_n > 10) {
        // make sure the message is valid
    }
}

// ============================================================================
int main(int argc, char** argv)
{
    ros::init(argc, argv, "serial_manager");
    ros::NodeHandle nh;
    ros::NodeHandle pnh("~");

    SerialManager serial_manager(nh, pnh);

    // set loop rate to be 500 Hz, note this should be equal to or higher
    // than the Arduino loop frequency
    ros::Rate loop_rate(500);
    while (!ros::isShuttingDown())
    {
        serial_manager.update();

        ros::spinOnce();
        loop_rate.sleep();
    }
}
