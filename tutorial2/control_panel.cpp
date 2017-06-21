#include "control_panel.h"
#include "ui_control_panel.h"

control_panel::control_panel(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::control_panel)
{
    ui->setupUi(this);
}

control_panel::~control_panel()
{
    delete ui;
}
