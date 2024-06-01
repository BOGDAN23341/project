from PyQt5.QtWidgets import (QLabel, QPushButton, QApplication,QWidget,QVBoxLayout,QRadioButton ) 


app = QApplication([])
window =QWidget()   
window.resize(200,200)

text = QLabel('zr dfc pdfnb')
button = QPushButton('обчисліть')
option1 = QRadioButton('Варіант 1')
option2 = QRadioButton('Варіант 2')
option3 = QRadioButton('Варіант 3')
option4 = QRadioButton('Варіант 4')
text1 = QLabel('dfif dslgjdslm')
 


layout = QVBoxLayout()
layout.addWidget(text)
layout.addWidget(option1)
layout.addWidget(option2)
layout.addWidget(option3)
layout.addWidget(option4)
layout.addWidget(button)
layout.addWidget(text1)
window.setLayout(layout)

def click():
    if option2.isChecked():
         text1.setText("правильно")
    else:
         text1.setText("неправильно")


style ="""
    QPushButton {
    background-color: red;
    color: grey;
    font-size: 20px;
    }
    """





window.setStyleSheet(style)
button.clicked.connect(click)
window.show()
app.exec_()

