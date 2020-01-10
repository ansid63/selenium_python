from selenium import webdriver
import time
import math



try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()


    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    print("Тест успешно завершен. 10 сек на закрытие браузера...")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()