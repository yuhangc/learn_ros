#ifndef CONTROL_PANEL_H
#define CONTROL_PANEL_H

#include <QMainWindow>

namespace Ui {
class control_panel;
}

class control_panel : public QMainWindow
{
    Q_OBJECT

public:
    explicit control_panel(QWidget *parent = 0);
    ~control_panel();

private:
    Ui::control_panel *ui;
};

#endif // CONTROL_PANEL_H
