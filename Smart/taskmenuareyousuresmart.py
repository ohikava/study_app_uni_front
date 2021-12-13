from Dumb.task_menu_are_you_sure import Ui_Form as TaskMenuAreYouSure
import sys
from PyQt5 import QtWidgets


class TaskMenuAreYouSureSmart(QtWidgets.QDialog, TaskMenuAreYouSure):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.send)

    def send(self):
        # TODO send a data to server
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TaskMenuAreYouSureSmart()
    window.show()
    app.exec_()
