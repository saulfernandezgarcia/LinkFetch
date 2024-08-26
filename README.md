# LinkFetch!
Yes, you heard that right! **LinkFetch!** Have you ever been faced by the need of saving all your currently open tabs in your browser?

**LinkFetch** is your solution! These are some of the cases I thought about when developing it:
- you finished some research and want to save all the links from your currently open tabs in case you later on want to take a look at them or quickly share them.
- you have trouble copying and pasting the links for later use (who doesn't find it hard to select a link, after all? 😉)
- you realize that the many links you opened on your incognito/regular window are actually of your interest and that you would like to keep them.
- you want to save a copy of some links, but don't want to get into your very-neatly organized bookmarks (you have little time!)

## How does it work?

First, the script will check for currently opened browsers. As of now, it can detect Google Chrome, Mozilla Firefox, and Microsoft Edge. After this, you will be prompted with a numbered list.
For browser windows, the title of the process is that of the "active" tab plus the name of the browser itself. For example, say you have a Chrome window where there are three tabs:
- "https://github.com"
- "https://www.google.com"
- "https://saulfernandezgarcia.github.io"

If your last seen tab was "https://github.com", then the title of the window could be "GitHub: Let’s build from here · GitHub - Google Chrome". If your last seen tab was "https://saulfernandezgarcia.github.io", then your title would be different. 

Then, you will be prompted to choose one of the items of the list. If you'd like to exit, just enter the last option. If you opted for using *LinkFetch*, then keep on reading! After your choice is received, the script will begin introducing the keyboard shortcuts to arrive to the desired window and then will start copying the links. After iterating through all the open tabs in the chosen window, the script will take you back to the window from which the script was launched, print the links to screen, and store them into the folder "LinkFetch_Results" under the name "URL_LIST_[date]_[time]".

## Limitations and Considerations

- As of now, please make sure the last active tab of your chosen window is not duplicated. The script will end prematurely.
- Please refrain from having the same "active tab" on multiple windows. This will make localizing your desired window easier for you.
- In current development of an "emergency stop" mechanism.

## Acknowledgements

Thank you to the unittest documentation, psutil, pyautogui, pygetwindow, and pyperclip.

## Saúl's notes
*What was my motivation for this?*: 

Usually, when I use the browser to do some work, I like to, add the end of all, decide what links I would like to keep, close unwanted links, and copy-paste them to a .txt file. Since I am a fan of keyboard shortcuts, I usually went for the following chain of hotkeys: ctrl+l, ctrl+c, alt+tab, ctrl+v, alt+shift+tab, ctrl+tab, rinse and repeat. While I am fast with the shortcuts, if the number of links is high, it can get cumbersome. Thus, I decided to start this project! Besides, it served as the perfect excuse for me to read the unittest docs for python and follow through with TDD. 
(☞ﾟヮﾟ)☞☜(ﾟヮﾟ☜)