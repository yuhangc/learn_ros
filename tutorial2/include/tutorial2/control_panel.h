#ifndef CONTROL_PANEL_H
#define CONTROL_PANEL_H

#include <QMainWindow>

namespace Ui {
class ControlPanel;
}

class ControlPanel : public QMainWindow
{
    Q_OBJECT

public:
    explicit ControlPanel(QWidget *parent = 0);
    ~ControlPanel();

private:
    Ui::ControlPanel *ui;
};

#endif // CONTROL_PANEL_H
