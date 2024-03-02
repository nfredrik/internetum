Feature: Network Connection Verification

  Scenario: Check Detailed Network Connection
    Given my computer has a MAC address
    When I check for an IP address

    When I perform a DNS lookup for "www.google.com"
    Then I should receive a valid DNS response

    When I ping "www.google.com"
    Then I should receive a successful ping response

    When I check the nearest router
    Then I should receive a successful response

