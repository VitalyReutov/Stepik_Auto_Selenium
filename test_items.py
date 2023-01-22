import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_text_on_button(language):
    browser = webdriver.Chrome('/Users/vitaly/Downloads/chromedriver_mac_arm64-2/chromedriver')
    browser.get(language)
    WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-add-to-basket'))
    )
    text_on_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket').text
    time.sleep(5)
    if language == "es":
        assert text_on_button == "Añadir al carrito", "WRONG TEXT"
    if language == "fr":
        assert text_on_button == "Ajouter au panier", "WRONG TEXT"
    if language == "ru":
        assert text_on_button == "Добавить в корзину", "WRONG TEXT"
    browser.quit()