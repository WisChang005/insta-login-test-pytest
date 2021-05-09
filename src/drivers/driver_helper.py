import os
import platform

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from src import drivers


def get_chrome_driver():
    driver_bin_map = {
        "Windows": "chromedriver.exe",
        "Darwin": "chromedriver",
    }
    driver_path = os.path.join(drivers.get_path(), driver_bin_map[platform.system()])
    chrome_options = Options()
    chrome_options.add_argument("--lang=en")
    return Chrome(executable_path=driver_path, service_args=["--verbose"], options=chrome_options)
