Feature: Login
  Scenario: A valid user try to log in
    Given an instance of auth.User with this attributes
    """
    {
      "username": "test",
      "is_active": 1
    }
    """
    And set password f140.123456. to the user test
    When a POST request to /api/login/ is made with the body
    """
    {
      "username": "test",
      "password": "f140.123456."
    }
    """
    Then the REST response is successful
    And $.token is not empty

  Scenario: An invalid user is trying to log in
    Given an instance of auth.User with this attributes
    """
    {
      "username": "test",
      "is_active": 1
    }
    """
    And set password f140.123456. to the user test
    When a POST request to /api/login/ is made with the body
    """
    {
      "username": "test",
      "password": "f140.abc."
    }
    """
    Then the response is a bad requested