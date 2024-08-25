import pygetwindow as gw
import pyautogui as pg
import pyperclip

# from pywinauto import Application

class WindowManager:

    @staticmethod
    def obtain_tabs(w: gw.Window):

        WindowManager.locate_window(w)

        url_list = []

        first_url = WindowManager.copy_paste_link()
        url_list.append(first_url)
        WindowManager.next_tab()
        while True:
            new_url = WindowManager.copy_paste_link()
            if (new_url == first_url):
                break

            url_list.append(new_url)
            WindowManager.next_tab()

        print(url_list)

        return url_list

    @staticmethod
    def locate_window(w):
        i = 1
        while not WindowManager.is_desired_window_on_foreground(w):
            WindowManager.previous_window()

    @staticmethod
    def get_foreground_window():
        active_window = gw.getActiveWindow()
        return active_window

    @staticmethod
    def is_desired_window_on_foreground(desired_window: gw.Window):
        current_foreground = WindowManager.get_foreground_window()
        return current_foreground._hWnd == desired_window._hWnd

    #___________________________________________________________

    @staticmethod
    def previous_window():
        pg.hotkey("alt", "shift", "tab")

    @staticmethod
    def next_window():
        pg.hotkey("alt", "tab")
        #GOOD LORD FIX THIS, MAKE IT A REQUIREMENT TO HAVE THE TAB AS NEXT IMMEDIATE TAB

    @staticmethod
    def next_tab():
        pg.hotkey("ctrl", "tab")

    @staticmethod
    def previous_tab():
        pg.hotkey("ctrl", "shift", "tab")

    @staticmethod
    def copy_paste_link():
        pg.hotkey("ctrl", "l")
        pg.hotkey("ctrl", "c")
        return pyperclip.paste()

