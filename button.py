from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

import sys

class Example(QDialog):
    def __init__(self):
        super(Example, self).__init__()
        self.init()

    def init(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Simple')
        layout = QVBoxLayout()

        btn = QPushButton('我被按下了')
        btn.setCheckable(True)
        # btn.toggle()
        btn.clicked.connect(lambda: self.whichButton(btn))

        btn2 = QPushButton('图像按钮')
        btn2.setIcon(QIcon(QPixmap('/media/zhuzhu/ec114170-f406-444f-bee7-a3dc0a86cfa2/下载/icon.png')))
        btn2.clicked.connect(lambda: self.whichButton(btn2))

        btn3 = QPushButton('不可用的按钮')
        btn3.setEnabled(False)

        btn4 = QPushButton('&默认按钮')
        btn4.setDefault(True)
        btn4.clicked.connect(lambda:self.whichButton(btn4))

        layout.addWidget(btn)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        self.setLayout(layout)
        self.show()

    def whichButton(self, btn):
        print(btn.text())

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
