Feature: User Login
  As the System Owner
  I want users to be able to login
  so that system can identify individual users
  and personalise services accordingly

  Scenario: Existing user
    Given at the login screen
    When an existing user submits the correct username and password
    Then the system should return "Success" as the authentication status of the user

  Scenario: Existing user (wrong password)
    Given at the login screen
    When an existing user submits the incorrect username and password
    Then the system should return "Fail" as the authentication status of the user

  Scenario: Unknown user
    Given at the login screen
    When an unknown user submits some username and password
    Then the system should return "Fail" as the authentication status of the user
