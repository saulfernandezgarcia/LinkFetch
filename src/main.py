from src.utils.browser_finder import BrowserFinder

import pygetwindow as gw

def main():

    print(BrowserFinder.active_browsers())

    browserWindowList = (gw.getWindowsWithTitle("Chrome")
                         + gw.getWindowsWithTitle("Firefox")
                         + gw.getWindowsWithTitle("Edge"))
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
                #ObtainTabs(browserWindowDict[choiceId])
                pass
            else:
                raise ValueError("Please introduce a number from the selection")


        break

if __name__ == "__main__":
    main()

