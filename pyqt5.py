import sys
from PyQt5.QtWidgets import QDialog,QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Örnek")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.label1 = QLabel("Hello")
        self.label2 = QLabel("World")
        self.label3 = QLabel("0")
        self.label4 = QLabel("Ana Menü")

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.label4)

        self.btn_increase = QPushButton("Arttır")
        self.btn_decrease = QPushButton("Azalt")
        self.btn_settings = QPushButton("Ayarlar Menüsü")

        self.btn_increase.clicked.connect(self.increase_value)
        self.btn_decrease.clicked.connect(self.decrease_value)
        self.btn_settings.clicked.connect(self.show_settings_menu)

        self.layout.addWidget(self.btn_increase)
        self.layout.addWidget(self.btn_decrease)
        self.layout.addWidget(self.btn_settings)

        self.value = 0

        self.setLayout(self.layout)

    def increase_value(self):
        self.value += 1
        self.label3.setText(str(self.value))

    def decrease_value(self):
        self.value -= 1
        self.label3.setText(str(self.value))

    def show_settings_menu(self):
        settings_menu = SettingsMenu(self)
        settings_menu.exec_()

class SettingsMenu(QDialog):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.setWindowTitle("Ayarlar Menüsü")

        self.layout = QVBoxLayout()

        self.label1 = QLabel("Ana Menü")
        self.label2 = QLabel("Nem Değeri")
        self.label3 = QLabel("Sıcaklık Değeri")
        self.label4 = QLabel("Çıkış")

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.label4)

        self.btn_up = QPushButton("Yukarı")
        self.btn_down = QPushButton("Aşağı")
        self.btn_select = QPushButton("Seç")

        self.btn_up.clicked.connect(self.move_up)
        self.btn_down.clicked.connect(self.move_down)
        self.btn_select.clicked.connect(self.select_option)

        self.layout.addWidget(self.btn_up)
        self.layout.addWidget(self.btn_down)
        self.layout.addWidget(self.btn_select)

        self.setLayout(self.layout)

        self.selected_option = 1

    def move_up(self):
        self.selected_option = max(1, self.selected_option - 1)
        self.update_labels()

    def move_down(self):
        self.selected_option = min(4, self.selected_option + 1)
        self.update_labels()

    def update_labels(self):
        self.label1.setText("Ana Menü" if self.selected_option == 1 else "")
        self.label2.setText("Nem Değeri" if self.selected_option == 2 else "")
        self.label3.setText("Sıcaklık Değeri" if self.selected_option == 3 else "")
        self.label4.setText("Çıkış" if self.selected_option == 4 else "")

    def select_option(self):
        if self.selected_option == 1:
            self.parent.label4.setText("Ana Menü")
        elif self.selected_option == 2:
            self.parent.label4.setText("Nem Değeri")
        elif self.selected_option == 3:
            self.parent.label4.setText("Sıcaklık Değeri")
        elif self.selected_option == 4:
            self.parent.label4.setText("Çıkış")

        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
