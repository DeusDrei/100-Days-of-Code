from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL = "email"
ACCOUNT_PASSWORD = "password"
PHONE = "phone number"


def abort_application():
    close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    discard_button = driver.find_elements(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

reject_button = driver.find_element(By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_button.click()

email_field = driver.find_element(By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

all_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        phone = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            continue
        else:
            submit_button.click()

        close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        continue

driver.quit()
