Feature: HTTP Methods Testing different HTTP verbs

  Background:
    Given setup for http methods

  Scenario: delete
    When we delete
    Then we should get a 200 status code

  Scenario: get
    When we get
    Then we should get a 200 status code


  Scenario: patch
    When we patch
    Then we should get a 200 status code

  Scenario: post
    When we post
    Then we should get a 200 status code

  Scenario: put
    When we put
    Then we should get a 200 status code