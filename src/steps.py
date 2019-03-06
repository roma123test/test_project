from xml.etree import ElementTree

import requests

from src.constants import PATH_TO_XML_FILE


class Steps:
    # additional methods
    def check_status_code(self, response, expected_code):
        assert (response.status_code == expected_code), \
            "Required {} Response Code, but actual is {}".format(expected_code, response.status_code)

    def check_response_body_xml(self, response):
        assert response.headers['content-type'] == 'application/xml'

    def parse_xml_file(self, file_name):
        exp_dict = {}
        path = PATH_TO_XML_FILE + '{}'.format(file_name)
        elem = ElementTree.parse(path).getroot()
        for item in elem.findall('./*'):
            exp_dict[item.tag] = item.text
        return exp_dict

    # main methods
    def check_authorization(self, url, expected_message, expected_status_code):
        # send GET request
        response = requests.get(url)
        # check that Status Code is 401
        self.check_status_code(response, expected_status_code)
        # verify Response message
        assert (str(response.text.strip()) == str(
            expected_message)), "Response text {} doesn't match with expected".format(response.text)

    def get_and_verify_user_info(self, url, user, expected_status_code, expected_response):
        # create dictionary with elements, that should be in response
        expected_dict = self.parse_xml_file(expected_response)

        # send GET request to 'https://ws-test.keepit.com/users/zhc4v6-5ev7di-9hhhlm'
        response = requests.get(url, auth=(user.login, user.password))
        self.check_status_code(response, expected_status_code)
        self.check_response_body_xml(response)

        # parse response body and create dictionary with actual response elements
        root = ElementTree.fromstring(response.content)
        actual_dict = {}
        for item in root.findall('./*'):
            actual_dict[item.tag] = item.text

        # compare length of expected & actual dictionaries
        assert (expected_dict.__len__() == actual_dict.__len__()), \
            "Count of parameters on Response Body missmatch with expected"
        for act, exp in zip(actual_dict.items(), expected_dict.items()):
            assert (act == exp), "Missmatch parameter {} in Response Body".format(exp)

    def check_invalid_login(self, url, user, expected_message, expected_status_code):
        # send GET request with invalid login or password
        response = requests.get(url, auth=(user.login, user.password))
        # check that Status Code is 401
        self.check_status_code(response, expected_status_code)
        # verify Response message
        assert (str(response.text.replace('\n', '')) == str(
            expected_message)), "Response text doesn't match with expected"
