@regression
Feature: Contact Us Form Functionality

  As a user, I want to ensure the Contact Us form behaves as expected so that I can correctly and efficiently submit my inquiries.

  Background:
    Given the user navigates to the Contact Us page


  @smoke
  Scenario Outline: Form Submission scenarios
    When the user fills in "first_name" field with value "<first_name>"
    And the user fills in "last_name" field with value "<last_name>"
    And the user fills in "email" field with value "<email>"
    And the user fills in "message" field with value "<message>"
    And the user clicks the "<button>" button
    Then the user should see the expected message saying "<expected_message>"

    Examples:
      | first_name | last_name | email                    | message                | button | expected_message               |
      | Kumar      | Akshat    | kumar.akshat@example.com | This is a test message | SUBMIT | Thank You for your Message!    |
      | Kumar      | Akshat    | kumar.akshatexample.com  | This is a test message | SUBMIT | Error: Invalid email address   |
      | \n         | \n        | \n                       | \n                     | SUBMIT | Error: all fields are required |

  # Scenario: Submit form with missing fields
  #   When the user clicks the "SUBMIT" button
  #   Then the user should see an error message saying "Error: all fields are required"

  # Scenario: Submit form with invalid email address
  #   When the user fills in "first_name" field with value "Kumar"
  #   And the user fills in "last_name" field with value "Akshat"
  #   And the user fills in "email" field with value "kumar.akshatexample.com"
  #   And the user fills in "message" field with value "This is a test message!"
  #   And the user clicks the "SUBMIT" button
  #   Then the user should see an error message saying "Error: Invalid email address"

  Scenario: Reset the Contact Us form
    When the user fills in "first_name" field with value "Kumar"
    And the user fills in "last_name" field with value "Akshat"
    And the user fills in "email" field with value "kumar.akshat@example.com"
    And the user fills in "message" field with value "This is a test message!"
    And the user clicks the "RESET" button
    Then all fields in the form are cleared
