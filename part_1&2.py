from PySide2.QtWidgets import QApplication
import part_1, part_2

if __name__=='__main__':
    app = QApplication([])
    win = part_1.SQLClientWindow()
    conf = part_2.ConfigurationDialog()
    win.show()
    conf.show()
    app.exec_()