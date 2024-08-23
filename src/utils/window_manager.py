import pygetwindow as gw
import pyautogui as pg
import pyperclip

class WindowManager:
    @staticmethod
    def obtain_tabs(w: gw.Window):
        w.maximize()

        url_list = []
        url_list.append(WindowManager.copy_paste_link())
        WindowManager.next_tab()
        while True:
            new_url = WindowManager.copy_paste_link()
            WindowManager.next_tab()
            if (url_list[0] == new_url):
                break
            else:
                url_list.append(new_url)
        print(url_list)
        return url_list

    @staticmethod
    def next_tab():
        pg.hotkey("ctrl", "tab")

    @staticmethod
    def copy_paste_link():
        pg.hotkey("ctrl", "l")
        pg.hotkey("ctrl", "c")
        return pyperclip.paste()

