from src.constants import BASIC_URL, UNAUTHORIZED_MSG, UNAUTHORIZED, WRONG_CREDENTIALS_ERROR_MSG, \
    USER_WITH_WRONG_LOGIN


def test_check_authorization_is_possible(app):
    """ Verify that we can get '401 Unauthorized' Error
    with appropriate message in Response Body """
    app.steps.check_authorization(url=BASIC_URL, expected_message=UNAUTHORIZED_MSG,
                                  expected_status_code=UNAUTHORIZED)



def test_login_with_invalid_credentials(app):
    """ Verify Error message, when attempt to login with invalid credentials """
    app.steps.check_invalid_login(url=BASIC_URL, user=USER_WITH_WRONG_LOGIN,
                                  expected_message=WRONG_CREDENTIALS_ERROR_MSG,
                                  expected_status_code=UNAUTHORIZED)

