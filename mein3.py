from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QHBoxLayout,QMessageBox

app = QApplication([]) # "додаток", який запускає програму
window = QWidget() # головне вікно

# створення віджетів
line = QLineEdit()
button_add = QPushButton("добавити завдання")
list1 = QListWidget()
button_done = QPushButton("виконано")
button_open = QPushButton("відкрити")
# прикріплення на леяути
vertical = QVBoxLayout()
horisont = QHBoxLayout()

horisont.addWidget(button_done)
horisont.addWidget(button_open)

vertical.addWidget(line)
vertical.addWidget(button_add)
vertical.addWidget(list1)
vertical.addLayout(horisont)
window.setLayout(vertical)
def add():
    text = line.text()
    if text:
        list1.addItem(text)
        line.clear()
    else:
        QMessageBox.warning(window, "Помилка","Будь ласка, введіть щось")

def delete():
    selected = list1.selectedItems()
    if selected:
        for item in selected:
            list1.takeItem(list1.row(item))



button_done.clicked.connect(delete)
button_add.clicked.connect(add)





window.show() # показує вікно
app.exec_() # запускає "додаток" у виконання
