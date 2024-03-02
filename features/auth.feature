Feature: HTTP Methods Testing different HTTP verbs

  Background:
    Given setup for http methods

  Scenario: basic auth
    When we get basic auth
    Then we should get a Unauthorized

