import psutil

class BrowserFinder:

    def __init__(self, desired_browser):
        self.desired_browser = desired_browser
        self.browser_is_active = False
        if desired_browser is None:
            raise ValueError("The desired browser must be specified.")

    def choose_browser(self, desired):
        self.desired_browser = desired

    def is_browser_active(self):

        for process in psutil.process_iter(["name"]):
            if process.info["name"] == self.desired_browser:
                self.browser_is_active = True
                return True
        return False
