from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8888/map.html')
browser.save_screenshot('screenshot.png')
browser.quit()