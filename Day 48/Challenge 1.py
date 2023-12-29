from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

time = driver.find_elements(By.TAG_NAME, value="time")[5:]
event_name = driver.find_elements(By.CSS_SELECTOR, value="div.shrubbery li a")[5:10]
upcoming_events = {i: {"time": time[i].text, "name": event_name[i].text} for i in range(len(time))}
print(upcoming_events)

driver.quit()