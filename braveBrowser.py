from selenium import webdriver
import sys

# Assigning Path
driver_path = "/Users/bunny_codec/Library/Mobile Documents/com~apple~CloudDocs/Python_Dev/Selenium/drivers/chromedriver"
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

# Creating Options for Brave Browser
option = webdriver.ChromeOptions()
option.binary_location = brave_path

# Starting Brave Browser
browser = webdriver.Chrome(executable_path=driver_path, options=option)

# Launching Url
browser.get(sys.argv[1])