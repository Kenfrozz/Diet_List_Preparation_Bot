import os
import sys
import docx
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Düğme oluştur
        self.button = QPushButton("Klasörleri oluştur", self)
        self.button.clicked.connect(self.on_button_clicked)
        self.button.move(20, 20)
        self.button.resize(160,60)

    def on_button_clicked(self):
        # Düğmeye tıklandığında çalıştırılacak kod
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY1/21_25bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY1/26_29bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY1/30_33bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY1/34_37bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY2/21_25bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY2/26_29bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY2/30_33bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY2/34_37bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY3/21_25bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY3/26_29bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY3/30_33bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY3/34_37bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY4/21_25bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY4/26_29bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY4/30_33bmi")
        os.makedirs("DIETS/TWO_MEAL_DIETS/AY4/34_37bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY1/21_25bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY1/26_29bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY1/30_33bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY1/34_37bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY2/21_25bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY2/26_29bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY2/30_33bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY2/34_37bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY3/21_25bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY3/26_29bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY3/30_33bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY3/34_37bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY4/21_25bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY4/26_29bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY4/30_33bmi")
        os.makedirs("DIETS/THREE_MEAL_DIETS/AY4/34_37bmi")


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
