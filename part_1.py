from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton,QTextEdit, QTableWidget, QHeaderView
import part_2

class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('SQL Client')
        self.setMinimumSize(600,400)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.buttons_panel=ButtonsPanel()
        self.main_layout.addWidget(self.buttons_panel)

        self.notification_panel=QTextEdit()
        self.main_layout.addWidget(self.notification_panel)

        self.result_table=QTableWidget()
        self.result_table.setShowGrid(True)

        self.result_table=QTableWidget(5,3)
        self.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.main_layout.addWidget(self.result_table)

        self.configuration_dialog=part_2.ConfigurationDialog()
        self.show()
        self.configuration_dialog.show()


class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.button_layout=QHBoxLayout()
        self.setLayout(self.button_layout)
        buttons=[QPushButton('Configure'),QPushButton('Connect'),QPushButton('Disconnect')]
        for button in buttons:
            self.button_layout.addWidget(button)


if __name__=='__main__':
    app=QApplication([])
    win=SQLClientWindow()
    app.exec_()