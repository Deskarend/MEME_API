import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class AuthorizeEndpointEndpoint(BaseEndpoint):
    @allure.step('Authorize')
    def authorize(self, payload=None):
        self.response = requests.post(f'{self.BASE_URL}/authorize', json=payload)
        if self.response.status_code == 200:
            self.response_json = self.response.json()

    @allure.step('Getting authorization token')
    def get_authorization_token(self):
        return self.response_json.get('token')

    @allure.step('Check response of correct authorize request')
    def check_response_of_successful_authorize(self, payload):
        self.check_status_code_is_200()
        assert self.response_json.get('token'), 'Token is empty'
        assert self.response_json.get('user') == payload.get('name'), 'Name is incorrect'
