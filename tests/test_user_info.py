from src.constants import BASIC_URL, USER_BY_DEFAULT, SUCCESS


def test_user_parameters_in_response(app):
    """ Verify each Response Parameter are present & match with expected """
    app.steps.get_and_verify_user_info(url=BASIC_URL, user=USER_BY_DEFAULT, expected_status_code=SUCCESS,
                                       expected_response='expected_response.xml')
