"""Methods for check responses"""
import json
from tabnanny import check

from requests import Response


class checking():

    """Method for check a status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success!!! Status code = " + str(response.status_code))
        else:
            print("Failed!!! Status code = " + str(response.status_code))


    """Method for check required fields"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All required fields exist")

    """Method for check value required fields"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен!!!")

    """Method for check value required fields по заданному слову"""

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово " + search_word + " присутствует!!!")
        else:
            print("Слово " + search_word + " отсутствует!!!")