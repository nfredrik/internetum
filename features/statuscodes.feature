Feature: status code

  Background:
    Given setup for http methods

  Scenario: delete
    When setup delete to reply with 418
    Then we should this reply

