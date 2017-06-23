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

    double curr_x;
    double curr_y;
    double curr_theta;
    double curr_lin_vel;
    double curr_ang_vel;

    double desired_lin_vel;
    double desired_ang_vel;

    void pos_callback(const turtlesim::Pose& msg);

private slots:
    void main_update();
    void on_start_button_clicked();
    void on_stop_button_clicked();
};

#endif // CONTROL_PANEL_H
