from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_span = browser.find_element_by_id("num1")
    num2_span = browser.find_element_by_id("num2")
    num1 = num1_span.text
    num2 = num2_span.text
    sum = int(num1) + int(num2)

    print(sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum))


    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    print("Тест успешно завершен. 10 сек на закрытие браузера...")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()