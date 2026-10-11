import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_interface import Ui_DenZieher
from scraper import getEmaillist

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_DenZieher()
        self.ui.setupUi(self)
        self.ui.Anwenden.clicked.connect(self.choiceApproved)
    def choiceApproved(self):
        country = self.ui.LandDropBox.currentText()
        faction = self.ui.FraktionDropBox.currentText()
        weirdthing = self.ui.OrganDropBox.currentText()
        name = self.ui.NameInput.displayText()

        emaillist = getEmaillist(country,faction,weirdthing,name)
        self.text = "\n".join(emaillist)
        self.ui.OutputTextBox.setText(self.text)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
