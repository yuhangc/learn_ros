#include "control_panel.h"
#include "ui_control_panel.h"

ControlPanel::ControlPanel(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ControlPanel)
{
    ui->setupUi(this);
}

ControlPanel::~ControlPanel()
{
    delete ui;
}

//===========================================================================
void ControlPanel::Init()
{
    // initialize subscribers
    turtle_pose_sub_ = nh_.subscribe("/turtle1/pose", 1000, &ControlPanel::pos_callback, this);

    // initialize publishers
    cmd_vel_pub_ = nh_.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel",1000);
    ros::Rate loop_rate(10);

    // TODO: any other initialization

    // connect timer to update functon
    connect(&update_timer_, SIGNAL(timeout()), this, SLOT(main_update()));
    update_timer_.start(50);
}


void ControlPanel::pos_callback(const turtlesim::Pose& msg)
{
    curr_x = msg.x;
    curr_y = msg.y;
    curr_theta = msg.theta;
    curr_lin_vel = msg.linear_velocity;
    curr_ang_vel = msg.angular_velocity;
}

//===========================================================================
void ControlPanel::main_update()
{
    // spin ros
    ros::spinOnce();

    // publish the commanded velocity
    geometry_msgs::Twist command;
    command.linear.x = desired_lin_vel;
    command.angular.z = desired_ang_vel;
    cmd_vel_pub_.publish(command);

    //write current stats to the LCD numbers
    ui->position_x_disp->display(curr_x);
    ui->position_y_disp->display(curr_y);
    ui->position_theta_disp->display(curr_theta);
    ui->lin_vel_disp->display(curr_lin_vel);
    ui->ang_vel_disp->display(curr_ang_vel);
    
    // TODO: your code
}

void ControlPanel::on_start_button_clicked()
{
    //Get the desired velocities (from the text boxes)
    desired_lin_vel = ui->des_lin_vel->toPlainText().toDouble();
    desired_ang_vel = ui->des_ang_vel->toPlainText().toDouble();
}

void ControlPanel::on_stop_button_clicked()
{
    //set desired velocities to 0
    desired_lin_vel = 0;
    desired_ang_vel = 0;
}
