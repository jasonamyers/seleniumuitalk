from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time


def webdriver_setup():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    return driver


def load_demo_site(driver):
    driver.get("http://demo.cube-star.com")
    assert "Cube-Star" in driver.title
    return driver


def add_paperclips_to_cart(driver):
    driver.find_element_by_css_selector("img[alt=\"Put A Bird On It! Add some whimsey with CLIPIT Paper Clips\"]").click()
    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_css_selector("li.item.last > div.actions > button.button.btn-cart"))
    elem.click()


def start_checkout_post_add_to_cart(driver):
    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath("//button[@type='button']"))
    elem.click()


def process_checkout_as_guest(driver):
    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("login:guest"))
    elem.click()

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("onepage-guest-register-button"))
    elem.click()


def complete_billing_info(driver):
    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("billing:firstname"))
    elem.send_keys("Jason")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("billing:lastname"))
    elem.send_keys("Myers")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("billing:company"))
    elem.send_keys("Home")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("billing:email"))
    elem.send_keys("jason.myers@bordership.com")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("billing:street1"))
    elem.send_keys("117 Russel St")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("billing:city"))
    elem.send_keys("London")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("billing:postcode"))
    elem.send_keys("W1P6HQ")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("billing:telephone"))
    elem.send_keys("615-556-3180")

    elem = WebDriverWait(driver, 100).until(lambda driver: Select(driver.find_element_by_id("billing:country_id")))
    elem.select_by_visible_text("United Kingdom")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath("//form[@id='co-billing-form']/fieldset/ul/li[3]/label"))
    elem.click()

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("billing:use_for_shipping_no"))
    elem.click()

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_css_selector("#billing-buttons-container > button.button"))
    elem.click()


def complete_shipping_info(driver):
    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("shipping:firstname"))
    elem.send_keys("Jason")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("shipping:lastname"))
    elem.send_keys("Myers")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("shipping:company"))
    elem.send_keys("Work")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("shipping:street1"))
    elem.send_keys("117 Russel St")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("shipping:city"))
    elem.send_keys("London")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("shipping:postcode"))
    elem.send_keys("W1P6HQ")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("shipping:telephone"))
    elem.send_keys("6157966526")

    elem = WebDriverWait(driver, 100).until(lambda driver: Select(driver.find_element_by_id("shipping:country_id")))
    elem.select_by_visible_text("United Kingdom")

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_css_selector("#shipping-buttons-container > button.button"))
    elem.click()


def choose_shipping_method(driver):
    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("s_method_bordership_EU_STANDARD"))
    elem.click()

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_css_selector("#shipping-method-buttons-container > button.button"))
    elem.click()


def choose_check_payment_method(driver):
    time.sleep(3)

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id("p_method_checkmo"))
    elem.click()

    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_css_selector("#payment-buttons-container > button.button"))
    elem.click()


def complete_checkout(driver):
    elem = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_css_selector("button.button.btn-checkout"))
    elem.click()


def main():
    driver = webdriver_setup()
    load_demo_site(driver)
    add_paperclips_to_cart(driver)
    start_checkout_post_add_to_cart(driver)
    process_checkout_as_guest(driver)
    complete_billing_info(driver)
    complete_shipping_info(driver)
    choose_shipping_method(driver)
    choose_check_payment_method(driver)
    complete_checkout(driver)


if __name__ == "__main__":
    main()
