from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout 
from random import *

app = QApplication([])
window =QWidget()   
window.resize(200,200)
button = QPushButton("Натисни")
text = QLabel("привіт")

layout = QVBoxLayout()
layout.addWidget(text)
layout.addWidget(button)
window.setLayout(layout)


def click():
    n = randint(0,101)
    text.setText(str(n))

button.clicked.connect(click)

window.show()
app.exec_()