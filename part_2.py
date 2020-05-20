from PySide2.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QDialog

class LabeledTextField(QWidget):
    def __init__(self,text):
        QWidget.__init__(self)
        self.layout=QHBoxLayout()
        self.setLayout(self.layout)

        self.label=QLabel(text)
        self.line_edit=QLineEdit()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('Configuration')
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        labeledtextfields=[LabeledTextField('IP address'),LabeledTextField('User'),LabeledTextField('Password')]
        for labeledtextfield in labeledtextfields:
            self.layout.addWidget(labeledtextfield)

if __name__=='__main__':
    app=QApplication([])
    win=ConfigurationDialog()
    win.show()
    app.exec_()