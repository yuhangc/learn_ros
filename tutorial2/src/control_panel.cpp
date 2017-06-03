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
    // TODO: your code

    // initialize publishers
    // TODO: your code

    // TODO: any other initialization

    // connect timer to update functon
    connect(&update_timer_, SIGNAL(timeout()), this, SLOT(main_update()));
    update_timer_.start(50);
}

//===========================================================================
void ControlPanel::main_update()
{
    // spin ros
    ros::spinOnce();

    // publish the commanded velocity
    // TODO: your code
}
