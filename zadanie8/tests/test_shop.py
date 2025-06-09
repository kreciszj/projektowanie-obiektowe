import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.environ.get("SHOP_URL", "http://localhost:5173")


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument(f"--user-data-dir=/tmp/chrome-profile-{os.getpid()}")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


def open_home(driver):
    driver.get(BASE_URL)
    time.sleep(1)


def cart_link(driver):
    return driver.find_element(By.XPATH, "//nav//a[contains(text(),'Cart')]")


def open_cart(driver):
    cart_link(driver).click()


def open_payment(driver):
    try:
        driver.find_element(By.LINK_TEXT, "Payment").click()
    except Exception:
        driver.get(BASE_URL + "/payment")
    time.sleep(1)


def wait_for_alert(driver, timeout: int = 5):
    WebDriverWait(driver, timeout).until(EC.alert_is_present())
    return driver.switch_to.alert


def test_homepage_title(browser):
    open_home(browser)
    assert "Shop" in browser.title
    assert browser.find_element(By.TAG_NAME, "h2").text == "Products"
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_products_list_has_three_items(browser):
    open_home(browser)
    items = browser.find_elements(By.CSS_SELECTOR, "ul li")
    assert len(items) == 3
    buttons = browser.find_elements(By.CSS_SELECTOR, "ul li button")
    assert len(buttons) == 3
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_first_product_is_coffee(browser):
    open_home(browser)
    first = browser.find_elements(By.CSS_SELECTOR, "ul li")[0].text
    assert "Coffee" in first
    assert "12.5" in first


def test_second_product_is_tea(browser):
    open_home(browser)
    second = browser.find_elements(By.CSS_SELECTOR, "ul li")[1].text
    assert "Tea" in second
    assert "10" in second


def test_third_product_is_cookie(browser):
    open_home(browser)
    third = browser.find_elements(By.CSS_SELECTOR, "ul li")[2].text
    assert "Cookie" in third
    assert "5.7" in third


def test_add_first_product_to_cart_increases_count(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    assert "Cart (1)" in cart_link(browser).text
    open_cart(browser)
    assert "Coffee" in browser.find_elements(By.CSS_SELECTOR, "ul li")[0].text
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_cart_total_after_adding_first_product(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    open_cart(browser)
    total = browser.find_element(By.XPATH, "//p[contains(., 'Total')]").text
    assert "12.5" in total
    assert browser.find_element(By.TAG_NAME, "h2").text == "Cart"


def test_add_second_product(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[1].click()
    assert "Cart (1)" in cart_link(browser).text
    open_cart(browser)
    sec_prod = browser.find_elements(By.CSS_SELECTOR, "ul li")[0].text
    assert "Tea" in sec_prod
    assert "10 zł" in sec_prod


def test_cart_total_two_products(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    browser.find_elements(By.CSS_SELECTOR, "li button")[1].click()
    open_cart(browser)
    total = browser.find_element(By.XPATH, "//p[contains(., 'Total')]").text
    assert "22.5" in total
    items = browser.find_elements(By.CSS_SELECTOR, "ul li")
    assert len(items) == 2


def test_add_third_product(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[2].click()
    assert "Cart (1)" in cart_link(browser).text
    open_cart(browser)
    assert "Cookie" in browser.find_elements(By.CSS_SELECTOR, "ul li")[0].text


def test_cart_total_three_products(browser):
    open_home(browser)
    for i in range(3):
        browser.find_elements(By.CSS_SELECTOR, "li button")[i].click()
    open_cart(browser)
    total = browser.find_element(By.XPATH, "//p[contains(., 'Total')]").text
    assert "28.2" in total
    items = browser.find_elements(By.CSS_SELECTOR, "ul li")
    assert len(items) == 3
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_payment_disabled_when_cart_empty(browser):
    browser.get(BASE_URL + "/payment")
    btn = browser.find_element(By.TAG_NAME, "button")
    assert btn.get_attribute("disabled")
    assert "0" in browser.find_element(By.XPATH, "//p[contains(., 'Total')]").text
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_payment_enabled_with_products(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    open_payment(browser)
    WebDriverWait(browser, 5).until(lambda d: d.find_element(By.TAG_NAME, "button").is_enabled())
    assert browser.find_element(By.TAG_NAME, "button").is_enabled()
    assert browser.find_element(By.TAG_NAME, "select").get_attribute("value") == "card"


def test_clear_cart_after_payment(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    open_payment(browser)
    browser.find_element(By.TAG_NAME, "button").click()
    wait_for_alert(browser).accept()
    assert "Cart (0)" in cart_link(browser).text
    open_cart(browser)
    assert "empty" in browser.find_element(By.TAG_NAME, "p").text


def test_payment_alert(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    open_payment(browser)
    browser.find_element(By.TAG_NAME, "button").click()
    alert = wait_for_alert(browser)
    assert "Payment sent" in alert.text
    alert.accept()
    open_cart(browser)
    assert "Total: 0 zł" in browser.find_element(By.TAG_NAME, "p").text


def test_switch_payment_method(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    open_payment(browser)
    select = browser.find_element(By.TAG_NAME, "select")
    for option in select.find_elements(By.TAG_NAME, "option"):
        if option.get_attribute("value") == "cash":
            option.click()
    assert select.get_attribute("value") == "cash"
    assert browser.find_element(By.TAG_NAME, "button").is_enabled()
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_go_to_cart_from_menu(browser):
    open_home(browser)
    cart_link(browser).click()
    assert "Products" in browser.find_element(By.TAG_NAME, "h2").text
    assert browser.current_url.endswith("/cart")
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_go_to_payment_from_menu(browser):
    open_home(browser)
    browser.find_element(By.LINK_TEXT, "Payment").click()
    assert "Products" in browser.find_element(By.TAG_NAME, "h2").text
    assert browser.current_url.endswith("/payment")


def test_cart_shows_product_names(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    open_cart(browser)
    names = browser.find_elements(By.CSS_SELECTOR, "ul li")
    assert any("Coffee" in n.text for n in names)
    assert browser.find_element(By.TAG_NAME, "h2").text == "Products"


def test_cart_page_shows_total(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    open_cart(browser)
    total = browser.find_element(By.XPATH, "//p[contains(., 'Total')]").text
    assert "Total" in total
    assert "zł" in total
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_navigation_back_to_products(browser):
    browser.get(BASE_URL + "/cart")
    browser.find_element(By.LINK_TEXT, "Products").click()
    assert "Cart" in browser.find_element(By.TAG_NAME, "h2").text
    assert browser.current_url.rstrip("/") == BASE_URL.rstrip("/")


def test_add_duplicate_product(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    open_cart(browser)
    items = browser.find_elements(By.CSS_SELECTOR, "ul li")
    assert len(items) == 3
    assert sum("Coffee" in i.text for i in items) == 1


def test_cart_total_after_duplicates(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    browser.find_elements(By.CSS_SELECTOR, "li button")[0].click()
    assert "Cart (2)" in cart_link(browser).text
    open_cart(browser)
    total = browser.find_element(By.XPATH, "//p[contains(., 'Total')]").text
    assert "25" in total


def test_cart_count_after_duplicates(browser):
    open_home(browser)
    for _ in range(3):
        browser.find_elements(By.CSS_SELECTOR, "li button")[1].click()
    assert "Cart (3)" in cart_link(browser).text
    open_cart(browser)
    assert len(browser.find_elements(By.CSS_SELECTOR, "ul li")) == 3
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_payment_total_with_duplicates(browser):
    open_home(browser)
    for _ in range(2):
        browser.find_elements(By.CSS_SELECTOR, "li button")[2].click()
    open_payment(browser)
    WebDriverWait(browser, 5).until(
        lambda d: "11.4" in d.find_element(By.XPATH, "//p[contains(., 'Total')]").text
    )
    total = browser.find_element(By.XPATH, "//p[contains(., 'Total')]").text
    assert "11.4" in total
    assert browser.find_element(By.TAG_NAME, "button").is_enabled()


def test_cart_empty_message(browser):
    browser.get(BASE_URL + "/cart")
    text = browser.find_element(By.TAG_NAME, "p").text
    assert "empty" in text
    assert "Total" in browser.find_element(By.XPATH, "//p[contains(., 'Total')]").text
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_cart_count_zero_after_payment(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[1].click()
    open_payment(browser)
    browser.find_element(By.TAG_NAME, "button").click()
    wait_for_alert(browser).accept()
    assert "Cart (0)" in cart_link(browser).text
    open_cart(browser)
    assert "Total: 0 zł" in browser.find_element(By.TAG_NAME, "p").text


def test_payment_select_cash(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[1].click()
    open_payment(browser)
    select = browser.find_element(By.TAG_NAME, "select")
    select.find_elements(By.TAG_NAME, "option")[1].click()
    assert select.get_attribute("value") == "cash"
    assert len(select.find_elements(By.TAG_NAME, "option")) == 2
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_payment_select_card(browser):
    open_home(browser)
    browser.find_elements(By.CSS_SELECTOR, "li button")[1].click()
    open_payment(browser)
    select = browser.find_element(By.TAG_NAME, "select")
    assert select.get_attribute("value") == "card"
    assert len(select.find_elements(By.TAG_NAME, "option")) == 2
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text


def test_add_products_and_pay(browser):
    open_home(browser)
    for i in range(3):
        browser.find_elements(By.CSS_SELECTOR, "li button")[i].click()
    open_payment(browser)
    browser.find_element(By.TAG_NAME, "button").click()
    wait_for_alert(browser).accept()
    assert "Cart (0)" in cart_link(browser).text
    open_cart(browser)
    assert "Total: 0 zł" in browser.find_element(By.TAG_NAME, "p").text
    nav = browser.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    links = nav.find_elements(By.TAG_NAME, "a")
    assert len(links) == 3
    assert "Cart" in links[1].text
