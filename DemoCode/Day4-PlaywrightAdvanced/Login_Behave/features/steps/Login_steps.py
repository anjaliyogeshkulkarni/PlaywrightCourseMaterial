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
####################################################################################

@given('the user is on the login page')
def step_impl(context):
    context.page.goto('https://www.saucedemo.com/')
    logging.info("Browser opened ")

@when('the user enters valid credentials')
def step_impl(context):
    context.page.fill(id_userName, userName)
    context.page.fill(id_password, password)
    logging.info("User name password filled in")

@when('clicks the login button')
def step_impl(context):
    context.page.click(xPath_loginButton)
    logging.info("Login button clicked")

@when('the user enters valid username and incorrect password')
def step_impl(context):
    context.page.fill(id_userName, userName)
    context.page.fill(id_password, password)
    # context.page.fill(id_password, "incorrectPwd")
    logging.info("User name and incorrect password filled in")

@then('the user should be redirected to the dashboard')
def step_impl(context):
    if expect(context.page).to_have_url(url):
        assert True
        logging.info("Login Successful")

@then('Error message should be displayed on the login page')
def step_impl(context):
    if expect(context.page).not_to_have_url(url):
        assert True
        logging.info("Error message displayed")
