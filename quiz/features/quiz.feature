Feature: Answer the quiz
    In order to feed our stats related to the python survey
    As cigna members
    We need to answer the quiz

    Scenario: User provides bad lanid
        Given I go to the "http://127.0.0.1:16500/" page
        When I insert the lanid "diu344" and try to go to the next screen
        Then the error message "Enter a valid value." is shown


    Scenario: User provides good lanid
        Given I go to the "http://127.0.0.1:16500/" page
        When I insert the lanid "M23455" and try to go to the next screen
        Then the url should be "http://127.0.0.1:16500/do-quiz/M23455/" page

    Scenario: User check quiz has question
        Given I go to the "http://127.0.0.1:16500/" page
        When I insert the lanid "M23455" and try to go to the next screen
        Then the page should contain one question 
