Feature: Convert
  Scenario: we can convert currencies
    Given we are looking at the home page
    When I convert 10 TTD to ZMW
    And I click on Convert button
    Then the following result should be returned
      | result |
      | 26.38 |