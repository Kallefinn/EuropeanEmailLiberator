import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QObject, QThreadPool, Signal, QRunnable
from ui_interface import Ui_DenZieher
from scraper import getEmaillist

class DataCarriage(QObject):
    finished = Signal(object)


class Worker(QRunnable):

    def __init__(self,country,faction):
        super().__init__()
        self.carrier = DataCarriage() 
        self.country = country
        self.faction = faction
    def run(self):
        print("getthosemails called")
        emaillist = getEmaillist(self.country,self.faction)
        self.carrier.finished.emit(emaillist)

        


class MainWindow(QMainWindow):
    thready = QThreadPool()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_DenZieher()
        self.ui.setupUi(self)
        self.ui.Anwenden.clicked.connect(self.choiceApproved)
    def choiceApproved(self):
        self.ui.OutputTextBox.setText("right on it Boss!")

        country = self.ui.LandDropBox.currentText()
        faction = self.ui.FraktionDropBox.currentText()
        dobby = Worker(country,faction)
        dobby.carrier.finished.connect(self.workerAnswer)
        self.thready.start(dobby)
        print("thrread sent off")
        

    def workerAnswer(self,emaillist):
        print("worker returned")
        self.text = emaillist
        self.text = "\n".join(emaillist)
        self.ui.OutputTextBox.setText(self.text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
