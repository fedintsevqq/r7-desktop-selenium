from configs.config import ROOT_DIR

def get_driver(platform):
    chromedriver_path = None
    if platform == "linux" or platform == "linux2":
        chromedriver_path = ROOT_DIR + r'/utils/linux/chromedriver'
    elif platform == "darwin":
        chromedriver_path = ROOT_DIR + r'/utils/mac/chromedriver'
    elif platform == "win32":
        chromedriver_path = ROOT_DIR + r'/utils/windows/chromedriver.exe'
    return chromedriver_path