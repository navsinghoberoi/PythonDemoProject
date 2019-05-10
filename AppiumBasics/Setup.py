from appium import webdriver

class Setup:
    def setup_android_session(self,noreset):
        desired_caps = {}
        desired_caps['autoGrantPermissions'] = True
        desired_caps['platformName'] = 'Android'
        desired_caps['appiumVersion'] = '1.4.16'
        desired_caps['deviceName'] = 'Android'
        desired_caps['app'] = '/Users/navpreetsingh/Downloads/app-qa-3.6.1-qa.apk'
        desired_caps['launchApp'] = 'app.goplus.in.myapplication'
        desired_caps['fullReset'] = False
        desired_caps['noReset'] = noreset
        desired_caps['appWaitActivity'] = 'app.goplus.in.myapplication.*'

        driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        print("Appium session has been initiated")
        return driver



