import psutil

class BrowserFinder:

    browser_dict = {"chrome.exe" : "Chrome", "firefox.exe":"Firefox", "edge.exe":"Edge"}

    @staticmethod
    def is_browser_active(desired_browser):
        '''
        Check if desired browser is active.
        :return:
        '''
        for process in psutil.process_iter(["name"]):
            if process.info["name"] == desired_browser:
                return True
        return False

    @staticmethod
    def active_browsers():
        active_browsers = {}

        for process in psutil.process_iter(["name"]):
            if process.info["name"] in BrowserFinder.browser_dict:
                active_browsers[process.info["name"]] = BrowserFinder.browser_dict[process.info["name"]]
        return active_browsers


