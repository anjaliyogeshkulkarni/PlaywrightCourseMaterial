@regression
Feature: Add To Cart

@positive
  Scenario: Add To Cart
    Given the user is on the login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should be redirected to the dashboard
    Then clicks on the Add To Cart button for Backpack prodcut
    Then the product gets added to cart
