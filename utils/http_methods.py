import allure
import requests

from utils.logger import logger

"""List of HTTP methods"""

class http_methods():
    headers = {'Content-Type' : 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            logger.add_request(url, method="GET")
            result = requests.get(url, headers=http_methods.headers, cookies=http_methods.cookie)
            logger.add_response(result)
            return result


    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            logger.add_request(url, method="DELETE")
            result = requests.delete(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            logger.add_response(result)
            return result