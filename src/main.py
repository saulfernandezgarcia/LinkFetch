from src.utils.browser_finder import BrowserFinder
from src.utils.window_manager import WindowManager

import pygetwindow as gw

def main_menu():

    print(BrowserFinder.active_browsers())

    browserWindowList = []
    for browserName in BrowserFinder.browser_dict.values():
        browserWindowList += gw.getWindowsWithTitle(browserName)

    browserWindowDict = dict(zip(range(len(browserWindowList)), browserWindowList))

    while True:
        if len(browserWindowDict) > 0:
            print("\nWelcome! We have detected the following browser windows: ")
            i = 0

            for k,v, in browserWindowDict.items():
                print("{} - {}".format(k, v.title))
                i += 1
            print("{} - Exit".format(i))

            print("Please choose which window you wish to have the tab links extracted from.")
            choiceId = int(input("Enter your browser choice: "))

            if (choiceId in browserWindowDict or choiceId == len(browserWindowDict)):
                WindowManager.obtain_tabs(browserWindowDict[choiceId])
            else:
                raise ValueError("Please introduce a number from the selection")
        else:
            print("No active browser windows were detected.")
        break



if __name__ == "__main__":
    main_menu()

'''
pyautogui
pyperclip
psutil
pygetwindow
Consider: selenium
'''