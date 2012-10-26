from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time


def webdriver_setup():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    return driver


def load_test_site(driver):
    driver.get("http://demo.cube-star.com")
    time.sleep(3)


def add_paperclips_to_cart(driver):
    driver.find_element_by_css_selector("img[alt=\"Put A Bird On It! Add some whimsey with CLIPIT Paper Clips\"]").click()
    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item.last > div.actions > button.button.btn-cart"))
    elem.click()


def add_multiple_items_to_cart(driver):
    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("Blonde Stripes")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item > div.actions > button.button.btn-cart"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("av club pennant")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item > div.actions > button.button.btn-cart"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("candy apple")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath("(//button[@type='button'])[2]"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("cotton candy")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item.last > div.actions > button.button.btn-cart"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("colored smencils")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item.last > div.actions > button.button.btn-cart"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("bunny paper clips")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item > div.actions > button.button.btn-cart"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("flocked wallpaper")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item > div.actions > button.button.btn-cart"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("stripes quad")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item > div.actions > button.button.btn-cart"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("ysbael / sophie")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item > div.actions > button.button.btn-cart"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("search"))
    elem.send_keys("chocolate chip cookie")

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("div.form-search > button.button"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("li.item.last > div.actions > button.button.btn-cart"))
    elem.click()


def start_checkout_post_add_to_cart(driver):
    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath("//button[@type='button']"))
    elem.click()


def process_checkout_as_guest(driver):
    WebDriverWait(driver, 300).until(lambda driver : driver.find_element_by_id("login:guest").is_displayed())
    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("login:guest"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("onepage-guest-register-button"))
    elem.click()


def complete_billing_info(driver, address, test_type):
    WebDriverWait(driver, 300).until(lambda driver : driver.find_element_by_id("billing:firstname").is_displayed())
    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:firstname"))
    elem.send_keys(address['billing_firstname'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:lastname"))
    elem.send_keys(address['billing_lastname'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:company"))
    elem.send_keys(address['billing_company'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:email"))
    elem.send_keys(address['billing_email'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:street1"))
    elem.send_keys(address['billing_address1'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:street2"))
    elem.send_keys(address['billing_address2'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:city"))
    elem.send_keys(address['billing_city'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:postcode"))
    elem.send_keys(address['billing_postal_code'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:telephone"))
    elem.send_keys(address['billing_telephone'])

    elem = WebDriverWait(driver, 10).until(lambda driver : Select(driver.find_element_by_id("billing:country_id")))
    elem.select_by_visible_text(address['billing_country'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath("//form[@id='co-billing-form']/fieldset/ul/li[3]/label"))
    elem.click()

    if address['billing_country'] in ['United States', 'Spain', 'Canada']:
        elem = WebDriverWait(driver, 10).until(lambda driver : Select(driver.find_element_by_id("billing:region_id")))
        elem.select_by_visible_text(address['billing_state'])

    if test_type in ['test_domestic_shipping_fail']:
        elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:use_for_shipping_no"))
        elem.click()
    else:
        elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("billing:use_for_shipping_yes"))
        elem.click()


    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("#billing-buttons-container > button.button"))
    elem.click()


def complete_shipping_info(driver, address):

    WebDriverWait(driver, 300).until(lambda driver : driver.find_element_by_id("shipping:firstname").is_displayed())
    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("shipping:firstname"))
    elem.send_keys(address['shipping_firstname'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("shipping:lastname"))
    elem.send_keys(address['shipping_lastname'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("shipping:company"))
    elem.send_keys(address['shipping_company'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("shipping:street1"))
    elem.send_keys(address['shipping_address1'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("shipping:street2"))
    elem.send_keys(address['shipping_address2'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("shipping:city"))
    elem.send_keys(address['shipping_city'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("shipping:postcode"))
    elem.send_keys(address['shipping_postal_code'])

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("shipping:telephone"))
    elem.send_keys(address['shipping_telephone'])

    elem = WebDriverWait(driver, 10).until(lambda driver : Select(driver.find_element_by_id("shipping:country_id")))
    elem.select_by_visible_text(address['shipping_country'])

    if address['shipping_country'] in ['United States', 'Spain', 'Canada']:
        elem = WebDriverWait(driver, 10).until(lambda driver : Select(driver.find_element_by_id("shipping:region_id")))
        elem.select_by_visible_text(address['shipping_state'])


    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("#shipping-buttons-container > button.button"))
    elem.click()


def choose_shipping_method(driver, country):

    shipping_id = 's_method_bordership_FEDEX_PRIORITY'

    if country == 'Australia':
        shipping_id = 's_method_bordership_AU_STANDARD'

    if country in ['Spain', 'Germany']:
        shipping_id = 's_method_bordership_EU_STANDARD'

    if country in ['Canada']:
        shipping_id = 's_method_bordership_CPC_STANDARD'

    WebDriverWait(driver, 300).until(lambda driver : driver.find_element_by_id(shipping_id).is_displayed())

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id(shipping_id))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("#shipping-method-buttons-container > button.button"))
    elem.click()


def choose_check_payment_method(driver):



    WebDriverWait(driver, 300).until(lambda driver : driver.find_element_by_id("p_method_checkmo").is_displayed())
    elem = WebDriverWait(driver, 300).until(lambda driver : driver.find_element_by_id("p_method_checkmo"))
    elem.click()

    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("#payment-buttons-container > button.button"))
    elem.click()


def complete_checkout(driver):
    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("button.button.btn-checkout"))
    elem.click()


def validate_checkout_success(driver):
    WebDriverWait(driver, 300).until(lambda driver : driver.find_element_by_css_selector("h2.sub-title").is_displayed())
    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("h2.sub-title"))
    if elem.text == 'Thank you for your purchase!':
        return True
    return False


def take_default_shipping_method(driver):
    elem = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector("#shipping-method-buttons-container > button.button"))
    elem.click()



def run_test(driver, test, test_type):
    if test_type in ['domestic_shipping_fail']:
        load_test_site(driver)
        add_paperclips_to_cart(driver)
        start_checkout_post_add_to_cart(driver)
        process_checkout_as_guest(driver)
        complete_billing_info(driver, test, test_type)
        complete_shipping_info(driver, test)
        take_default_shipping_method(driver)
        choose_check_payment_method(driver)
        complete_checkout(driver)
        return validate_checkout_success(driver)
    elif test_type in ['multiple_skus']:
        load_test_site(driver)
        add_multiple_items_to_cart(driver)
        start_checkout_post_add_to_cart(driver)
        process_checkout_as_guest(driver)
        complete_billing_info(driver, test, test_type)
        choose_shipping_method(driver, test['billing_country'])
        choose_check_payment_method(driver)
        complete_checkout(driver)
        return validate_checkout_success(driver)
    else:
        load_test_site(driver)
        add_paperclips_to_cart(driver)
        start_checkout_post_add_to_cart(driver)
        process_checkout_as_guest(driver)
        complete_billing_info(driver, test, test_type)
        choose_shipping_method(driver, test['billing_country'])
        choose_check_payment_method(driver)
        complete_checkout(driver)
        return validate_checkout_success(driver)


