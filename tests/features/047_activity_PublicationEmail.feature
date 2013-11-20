Feature: PublicationEmail activity
  In order to use the PublicationEmail activity
  As a user
  I want to confirm the activity class can be used
  
  Scenario: Instantiate an PublicationEmail object
    Given I have imported a settings module
    And I have the settings environment <env>
    And I get the settings
    When I have the activity name PublicationEmail
    Then I have an activity object
    And I get a ejp provider from the activity object
    
  Examples:
    | env          
    | dev
    
  Scenario: Format the authors of an article for use in the email template
    Given I have imported a settings module
    And I have the settings environment <env>
    And I get the settings
    And I have the activity name PublicationEmail
    And I have an activity object
    And I have a document <document>
    When I get authors from the activity object
    Then I have the authors count <count>
    
  Examples:
    | env  | document                      | count
    | dev  | test_data/ejp_author_file.csv | 7
    
  Scenario: Format the editors of an article for use in the email template
    Given I have imported a settings module
    And I have the settings environment <env>
    And I get the settings
    And I have the activity name PublicationEmail
    And I have an activity object
    And I have a document <document>
    When I get editors from the activity object
    Then I have the editors count <count>
    
  Examples:
    | env  | document                      | count
    | dev  | test_data/ejp_editor_file.csv | 2