from time import sleep

import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

def wait_for(elem):
    pass

def main():
    driver = uc.Chrome(use_subprocess=True)
    driver.get("https://otv.verwalt-berlin.de/ams/TerminBuchen")

    # Page 1
    driver.find_element(By.LINK_TEXT, "Termin buchen").click()

    # Page 2
    elem = WebDriverWait(driver=driver, timeout=10.0).until(
        #EC.presence_of_element_located((By.ID, "xi-cb-1"))
        EC.element_to_be_clickable((By.ID, "xi-cb-1"))
    )
    elem.click()

    elem = driver.find_element(By.ID, "applicationForm:managedForm:proceed")
    elem.click()

    # Page 3
    # Select 1
    elem = WebDriverWait(driver=driver, timeout=10.0).until(
        EC.presence_of_element_located((By.ID, "xi-sel-400"))
    )
    select = Select(elem)
    sleep(0.3)
    select.select_by_value('160')

    # Select 2
    elem = WebDriverWait(driver=driver, timeout=10.0).until(
        EC.presence_of_element_located((By.ID, "xi-sel-422"))
    )
    select = Select(elem)
    sleep(0.1)
    select.select_by_value('1')

    # Select 3
    elem = WebDriverWait(driver=driver, timeout=10.0).until(
        EC.presence_of_element_located((By.ID, "xi-sel-427"))
    )
    select = Select(elem)
    sleep(0.1)
    select.select_by_value('2')

    # Servicewahl
    elem = WebDriverWait(driver=driver, timeout=10.0).until(
        EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Aufenthaltstitel - verlängern']"))
    )
    elem.click()

    # Studium und Ausbildung
    elem = WebDriverWait(driver=driver, timeout=10.0).until(
        EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Studium und Ausbildung']"))
    )
    elem.click()

    # Studium und Ausbildung - Auswahl
    elem = WebDriverWait(driver=driver, timeout=10.0).until(
        EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Aufenthaltserlaubnis zum Studium (§ 16b)']"))
    )
    elem.click()

    # Weiter
    elem = WebDriverWait(driver=driver, timeout=10.0).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='applicationForm:managedForm:proceed']"))
    )
    elem.click()

    # Schleife
    while True:
        try: 
            sp = WebDriverWait(driver=driver, timeout=10.0).until(
                EC.presence_of_element_located((By.XPATH, "//li[@class='errorMessage']"))
            )

            try:
                # Weiter
                el = WebDriverWait(driver=driver, timeout=10.0).until(
                    EC.element_to_be_clickable((By.ID, "applicationForm:managedForm:proceed"))
                )

                el.click()
            except:
                pass

        except TimeoutException:
            break

    sleep(100000)

if __name__ == '__main__':
    main()