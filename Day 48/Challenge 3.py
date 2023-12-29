from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

firstname = driver.find_element(By.NAME, value="fName")
firstname.send_keys("Alain Andrei")
lastname = driver.find_element(By.NAME, value="lName")
lastname.send_keys("Torno")
email = driver.find_element(By.NAME, value="email")
email.send_keys("alaintorno@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()
