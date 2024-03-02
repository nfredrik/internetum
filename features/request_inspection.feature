Feature: HTTP Methods Testing request inspection

  Background:
    Given setup for http methods

  Scenario: headers
    When we get headers
    Then we shold read stuff

  Scenario: ip
    When we get ip addr
    Then we verify ip addr

  Scenario: user agent
    When we get user agent
    Then we verify user agent