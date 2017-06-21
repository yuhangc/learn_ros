#include "control_panel.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    control_panel w;
    w.show();

    return a.exec();
}
