#ifndef SERIAL_MANAGER_H
#define SERIAL_MANAGER_H

#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float32MultiArray.h"

#include "CArduinoDevice.h"

class SerialManager
{
public:
    // constructor
    SerialManager(ros::NodeHandle &nh, ros::NodeHandle &pnh);

    // destructor
    ~SerialManager();

    // main update function
    void update();

private:
    // node handler
    ros::NodeHandle nh_;

    // subscriber and publisher
    ros::Publisher serial_data_pub;

    // arduino device
    CArduinoDevice* arduino;
};

#endif