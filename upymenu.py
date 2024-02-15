from lib.upymenu import Menu, MenuAction, MenuNoop
from data.lcd_library import LCDController


def action_callback():
    print("callback action choosen")

submenu = Menu("Submenu")
submenu_action_1 = MenuAction("Submenu Action", callback=action_callback)
submenu_action_2 = MenuAction("Submenu Action 1", callback=action_callback)
submenu.add_option(submenu_action_1)
submenu.add_option(submenu_action_2)

menu_action = MenuAction("Action", callback=action_callback)
menu = Menu("Main Menu")
menu.add_option(submenu)
menu.add_option(menu_action)
menu.add_option(MenuNoop("Nothing here"))

lcd = LCDController()
lcd = lcd.lcd

current_manu = menu.start(lcd)

menu.focus_next()
menu.focus_prev()

menu = menu.choose()

menu = menu.parent()