#ifndef CONTROL_PANEL_H
#define CONTROL_PANEL_H

#include <QMainWindow>
#include <QTimer>

#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"

namespace Ui {
class ControlPanel;
}

class ControlPanel : public QMainWindow
{
    Q_OBJECT

public:
    explicit ControlPanel(QWidget *parent = 0);
    ~ControlPanel();

    // for initialization
    void Init();
private:
    Ui::ControlPanel *ui;

    // Timer for GUI update
    QTimer update_timer_;

    // node handler
    ros::NodeHandle nh_;

    // subscribers
    ros::Subscriber turtle_pose_sub_;

    // publishers
    ros::Publisher cmd_vel_pub_;

private slots:
    void main_update();
};

#endif // CONTROL_PANEL_H
