import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Değişkenler
        self.counter = 0
        self.ayarlar_gosteriliyor = False

        # Ana pencere ayarları
        self.setWindowTitle("4 Satırlık Ekran Uygulaması")
        self.setGeometry(100, 100, 300, 200)

        # Widget'lar
        self.label_1 = QtWidgets.QLabel("Merhaba", self)
        self.label_2 = QtWidgets.QLabel("Dünya", self)
        self.label_3 = QtWidgets.QLabel(str(self.counter), self)
        self.button_arttir = QtWidgets.QPushButton("Arttır", self)
        self.button_azalt = QtWidgets.QPushButton("Azalt", self)
        self.button_ayarlar = QtWidgets.QPushButton("Ayarlar", self)

        # Widget düzenleme
        self.label_1.setGeometry(10, 10, 100, 20)
        self.label_2.setGeometry(10, 30, 100, 20)
        self.label_3.setGeometry(10, 50, 100, 20)
        self.button_arttir.setGeometry(120, 10, 100, 20)
        self.button_azalt.setGeometry(120, 30, 100, 20)
        self.button_ayarlar.setGeometry(120, 50, 100, 20)

        # Slotlar
        self.button_arttir.clicked.connect(self.deger_arttir)
        self.button_azalt.clicked.connect(self.deger_azalt)
        self.button_ayarlar.clicked.connect(self.ayarlari_goster)

        # Zamanlayıcı
        self.timer = QtCore.QTimer()
        self.timer.setInterval(2000)  # 2 saniyede bir
        self.timer.timeout.connect(self.deger_arttir)
        self.timer.start()

    def deger_arttir(self):
        self.counter += 1
        self.label_3.setText(str(self.counter))

    def deger_azalt(self):
        self.counter -= 1
        self.label_3.setText(str(self.counter))

    def ayarlari_goster(self):
        if not self.ayarlar_gosteriliyor:
            self.ayarlar_gosteriliyor = True

            # Ayarlar menüsü widget'ları
            self.label_ayarlar_1 = QtWidgets.QLabel("Ana Menü", self)
            self.label_ayarlar_2 = QtWidgets.QLabel("Nem: %", self)
            self.label_ayarlar_3 = QtWidgets.QLabel("Sıcaklık: %", self)
            self.label_ayarlar_4 = QtWidgets.QLabel("Çıkış", self)

            # Widget düzenleme
            self.label_ayarlar_1.setGeometry(10, 10, 100, 20)
            self.label_ayarlar_2.setGeometry(10, 30, 100, 20)
            self.label_ayarlar_3.setGeometry(10, 50, 100, 20)
            self.label_ayarlar_4.setGeometry(10, 70, 100, 20)

            # Butonları gizle
            self.button_arttir.hide()
            self.button_azalt.hide()
            self.button_ayarlar.hide()

            # Klavye kısayolları
            self.shortcut_yukari = QtWidgets.QShortcut(QtGui.QKeySequence("Up"), self)
            self.shortcut_yukari.activated.connect(self.ayarlar_yukari)
            self.shortcut_asagi = QtWidgets.QShortcut(QtGui.QKeySequence("Down"), self)
            self.shortcut_asagi.activated.connect(self.ayarlar_asagi)
            self.shortcut_enter = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self)
            self.shortcut_enter.activated.connect(self.ayarlari_sec)

    def ayarlari_gizle(self):
        if self.ayarlar_gosteriliyor:
            self.ayarlar_gosteriliyor = False

            # Ayarlar menüsü widget'larını gizle
            self.label_ayarlar_1.hide()
            self.label_ayarlar_2.hide()
            self.label_ayarlar_3.hide()
            self.label_ayarlar_4.hide()

            # Butonları göster
            self.button_arttir.show()
            self.button_azalt.show()
            self.button_ayarlar.show()

    def ayarlar_yukari(self):
        # Seçili satırı bir yukarı kaydır
        ...

    def ayarlar_asagi(self):
        # Seçili satırı bir aşağı kaydır
        ...

    def ayarlari_sec(self):
        # Seçilen satırdaki işlevi gerçekleştir
        ...

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
