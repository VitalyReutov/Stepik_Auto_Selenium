from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import math
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_search_example(selenium):
    selenium.get('http://suninjuly.github.io/explicit_wait2.html')

    element = WebDriverWait(selenium, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = selenium.find_element(By.TAG_NAME, 'button')
    button.click()
    selenium.execute_script("window.scrollBy(0, 100);")
    x_element = selenium.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    selenium.find_element(By.ID, 'answer').send_keys(y)
    selenium.find_element(By.XPATH, '/html/body/form/div/div/button').click()

    selenium.quit()

