from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

app = QApplication( [] )
win = QWidget()
win.setWindowTitle('Winner')
win.resize(300, 200)

# Створення віджетів
lb_txt1 = QLabel('Дізнайтесь переможця!')
lb_txt2 = QLabel("???")
btn = QPushButton("Сгенерувати")

# Розтошування віджетів

vline = QVBoxLayout()
vline.addWidget(lb_txt1, alignment=Qt.AlignCenter)
vline.addWidget(lb_txt2, alignment=Qt.AlignCenter)
vline.addWidget(btn, alignment=Qt.AlignCenter)

def random_win():
    lb_txt1.setText("Переможець:")
    num = randint(1, 100)
    lb_txt2.setText(str(num))

btn.clicked.connect(random_win)

win.setLayout(vline)

win.show()
app.exec_()