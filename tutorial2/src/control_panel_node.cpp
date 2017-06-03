#include <QApplication>

#include "control_panel.h"

// ============================================================================
int main(int argc, char** argv)
{
    // initialize node
    ros::init(argc, argv, "control_panel");

    // create a QApplication
    QApplication a(argc, argv);

    // create a main window object
    ControlPanel main_window;
    main_window.Init();

    // show the main window
    main_window.show();

    // exit
    return a.exec();
}
