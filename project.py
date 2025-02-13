import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import QTime,QTimer,Qt
class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.time=QTime(0,0,0,0)
        self.label = QLabel("00:00:00:00")
        self.start_button = QPushButton("start",self)
        self.stop_button = QPushButton("stop",self)
        self.reset_button= QPushButton("reset",self)
        self.init()
        self.setGeometry(300,200,300,400)
    def init(self):
        self.setWindowTitle("stopwatch")
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.reset_button)
        vbox.addWidget(self.stop_button)
        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)


        self.start_button.setStyleSheet("font-size:40px; color: green; ")
        self.stop_button.setStyleSheet("font-size:40px; color: green;")
        self.reset_button.setStyleSheet("font-size:40px; color: green;")
        self.setStyleSheet("background-color:black")
        self.label.setStyleSheet("font-size:150px; color: green;")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.label.setText(self.format(self.time))
    def format(self,time):
        hours= time.hour()
        minutes=time.minute()
        seconds = time.second()
        millisecond = time.msec() // 10
        return f"{hours}:{minutes}:{seconds}:{millisecond}"
    def update_display(self):
        self.time =self.time.addMSecs(10)
        self.label.setText(self.format(self.time))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch=Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

