class Menu:
    def __init__(self, title):
        self.title = title
        self.submenus = []

    def add_submenu(self, submenu):
        self.submenus.append(submenu)

    def show(self):
        while True:
            print("=== {} ===".format(self.title))
            for index, submenu in enumerate(self.submenus, start=1):
                print("{}. {}".format(index, submenu.title))
            print("0. Çıkış")
            choice = input("Seçiminizi yapın: ")

            if choice == '0':
                print("Programdan çıkılıyor...")
                break

            try:
                choice = int(choice)
                if 1 <= choice <= len(self.submenus):
                    selected_submenu = self.submenus[choice - 1]
                    selected_submenu.show()
                else:
                    print("Geçersiz seçim, tekrar deneyin.")
            except ValueError:
                print("Geçersiz giriş, tekrar deneyin.")

class SubMenu:
    def __init__(self, title):
        self.title = title
        self.value1 = 0
        self.value2 = 0
        self.increment_function1 = None
        self.increment_function2 = None
        self.decrement_function1 = None
        self.decrement_function2 = None

    def set_increment_function1(self, function):
        self.increment_function1 = function

    def set_increment_function2(self, function):
        self.increment_function2 = function

    def set_decrement_function1(self, function):
        self.decrement_function1 = function

    def set_decrement_function2(self, function):
        self.decrement_function2 = function

    def show(self):
        while True:
            print("=== {} ===".format(self.title))
            print("1. Değer 1 Artır")
            print("2. Değer 1 Azalt")
            print("3. Değer 2 Artır")
            print("4. Değer 2 Azalt")
            print("0. Geri")
            choice = input("Seçiminizi yapın: ")

            if choice == '0':
                print("Ana menüye geri dönülüyor...")
                break
            elif choice == '1' and self.increment_function1:
                self.increment_function1()
            elif choice == '2' and self.decrement_function1:
                self.decrement_function1()
            elif choice == '3' and self.increment_function2:
                self.increment_function2()
            elif choice == '4' and self.decrement_function2:
                self.decrement_function2()
            else:
                print("Geçersiz seçim, tekrar deneyin.")

# Değerler
value1 = 0
value2 = 0

# Değer 1 arttırma fonksiyonu
def increment_value1():
    global value1
    value1 += 1
    print("Değer 1 arttırıldı, yeni değer:", value1)

# Değer 1 azaltma fonksiyonu
def decrement_value1():
    global value1
    value1 -= 1
    print("Değer 1 azaltıldı, yeni değer:", value1)

# Değer 2 arttırma fonksiyonu
def increment_value2():
    global value2
    value2 += 1
    print("Değer 2 arttırıldı, yeni değer:", value2)

# Değer 2 azaltma fonksiyonu
def decrement_value2():
    global value2
    value2 -= 1
    print("Değer 2 azaltıldı, yeni değer:", value2)

# Ana menü oluştur
main_menu = Menu("Ana Menü")

# Alt menü oluştur
submenu = SubMenu("Değer Ayarlama")

# Artırma ve azaltma fonksiyonlarını alt menüye ekle
submenu.set_increment_function1(increment_value1)
submenu.set_decrement_function1(decrement_value1)
submenu.set_increment_function2(increment_value2)
submenu.set_decrement_function2(decrement_value2)

# Ana menüye alt menüyü ekle
main_menu.add_submenu(submenu)

# Menüyü göster
main_menu.show()
