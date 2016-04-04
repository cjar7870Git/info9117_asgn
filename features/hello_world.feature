Feature: Hello World
  As a user
  when I visit the landing page
  I want to be greeted by a "Hello World" message

  Scenario: Visit Landing Page
    Given the system is running
    When a User visits the Landing Page
    Then "Hello World" is returned to the User
