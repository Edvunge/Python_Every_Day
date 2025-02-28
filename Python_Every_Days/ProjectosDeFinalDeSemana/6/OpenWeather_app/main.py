from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout

# 6 open weather app
class Home(QWidget):
    def __init__(self):
        super().__init__()

    def settings(self):
        pass

    def initUI(self):
        pass

    def search_click(self):
        pass

    def get_weather(self):
        pass

if __name__ in "__main__":
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()