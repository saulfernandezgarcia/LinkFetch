from src.utils.browser_finder import BrowserFinder
from src.utils.window_manager import WindowManager
import os
import pygetwindow as gw
import datetime


def create_timestamped_file(content_list):
    folder_name = "LinkFetch_Results"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    current_date_time = datetime.datetime.now()
    filename = current_date_time.strftime("%Y%m%d_%H%M%S")

    filepath = os.path.join(folder_name, f"URL_LIST_{filename}.txt")

    with open(filepath, 'w') as output:
        for index, item in enumerate(content_list):
            if index < len(content_list)-1:
                output.write(str(item) + '\n')
            else:
                output.write(str(item))

    return filepath

def main_menu():

    # Will be used to latern on return to the script window
    script_window = WindowManager.get_foreground_window()

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
                url_list = WindowManager.obtain_tabs(browserWindowDict[choiceId])
                WindowManager.locate_window(script_window)
                print("-----------------------------------\nLinks found:")
                for url in url_list:
                    print(url)

                create_timestamped_file(url_list)

            else:
                raise ValueError("Please introduce a number from the selection")
        else:
            print("No active browser windows were detected.")
        break


if __name__ == "__main__":
    main_menu()