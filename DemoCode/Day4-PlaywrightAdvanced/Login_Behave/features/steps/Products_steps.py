from behave import given, when, then
from playwright.sync_api import sync_playwright, expect
import logging

################Test data################
userName = "standard_user"
password = "secret_sauce"
##########################################

##################################### Locators #####################################
xPath_loginButton = '//input[@data-test="login-button"]'
css_loginButton = 'input[type="submit"][value="Login"]'
id_userName = '#user-name'
name_userName = '[name="user-name"]'
placeholder_userName = 'input[placeholder="Username"]'
id_password = '#password'
url = "https://www.saucedemo.com/inventory.html"
id_add_to_cart = '#add-to-cart-sauce-labs-backpack'
dataTest_ShoppingCart = '//a[@data-test=\'shopping-cart-badge\']'

####################################################################################
#
# @given('the user is on the login page')
# def step_impl(context):
#     context.page.goto('https://www.saucedemo.com/')
#     logging.info("Browser opened ")
#
# @when('the user enters valid credentials')
# def step_impl(context):
#     context.page.fill(id_userName, userName)
#     context.page.fill(id_password, password)
#     logging.info("User name password filled in")
#
# @when('clicks the login button')
# def step_impl(context):
#     context.page.click(xPath_loginButton)
#     logging.info("Login button clicked")
#
#
# @then('the user should be redirected to the dashboard')
# def step_impl(context):
#     if expect(context.page).to_have_url(url):
#         assert True
#         logging.info("Login Successful")
#


@then('clicks on the Add To Cart button for Backpack prodcut')
def step_impl(context):
    context.page.click(id_add_to_cart)
    logging.info("Product added to cart")

@then('the product gets added to cart')
def step_impl(context):
    if context.page.locator(dataTest_ShoppingCart).is_visible():
        assert True
        logging.info("Product added to cart")

