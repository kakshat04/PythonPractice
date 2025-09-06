Feature: Status API Testing

  Background:
    Given The base URL is "https://goal-tracker-api.onrender.com/api/vi"

  @api
  Scenario: Check if the Status API returns "OPERATIONAL" on a successful request
    When A user sends a GET request to "/status" endpoint
    Then The response status code should be 200
    And The response should contain "OPERATIONAL"