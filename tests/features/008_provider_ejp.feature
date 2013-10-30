Feature: Use EJP data provider
  In order to use EJP as a data provider
  As a worker
  I want to parse files from local block storage device
  
  Scenario: Open a file with EJP provider' filesystem provider
    Given I have a tmp_base_dir <tmp_base_dir>
    And I have test name <test_name>
    And I get the current datetime
    And I get the tmp_dir from the world
    And I create a ejp provider
    And I have a document <document>
    When I parse author file the document with ejp
    And I get the ejp fs document
    Then I have the ejp document <ejp_document>

  Examples:
    | tmp_base_dir  | test_name             | document                      | ejp_document
    | tmp           | ejp_parse_author_file | test_data/ejp_author_file.csv | ejp_author_file.csv
