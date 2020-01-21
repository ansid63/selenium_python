import pytest
from selenium import webdriver
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


#

@pytest.mark.parametrize('links', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1",
                                   "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"])
class TestUfo():
    def test_find_text_by_link(self, browser, links):
        browser.implicitly_wait(7)

        link = f"https://stepik.org/lesson/{links}"
        browser.get(link)
        input_box = browser.find_element_by_css_selector(".ember-text-area")
        answer = str(math.log(int(time.time())))
        print(answer)

        input_box.send_keys(answer)
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()



        approve = browser.find_element_by_css_selector(".smart-hints__hint")
        recived_text = approve.text
        print(recived_text)

        assert "Correct!" in recived_text, "WTF wrong result"

