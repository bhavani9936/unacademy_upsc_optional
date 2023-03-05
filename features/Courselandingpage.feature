Feature: UPSC CSE-Optional
  Background:
    Given chrome is opened and UPSC course page is launched


  Scenario: To validate that user navigate to UPSC CSE-Optional course
    And user clicks Got it button


  Scenario: verify user clicks success stories
    And user clicks Got it button
    Then user clicks success stories
    And user is in success stories field

  Scenario: verify user clicks subsciption
    And user clicks Got it button
    Then user clicks subsciption button
    And user is in subscription field

  Scenario: verify user clicks store new
    Then user clicks store new button
    And user is in store new field

  Scenario: verify user clicks batch
    When user clicks store new button
    And user is in store new field
    Then user clicks batch button
    And user is in batch feild
