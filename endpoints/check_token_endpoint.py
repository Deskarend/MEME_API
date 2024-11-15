import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class CheckTokenEndpoint(BaseEndpoint):
    @allure.step('Check that token is alive')
    def check_token(self, token):
        self.response = requests.get(f'{self.BASE_URL}/authorize/{token}')

    @allure.step('Check response of correct check token request')
    def check_response_of_successful_check_token(self, payload):
        self.check_status_code_is_200()
        assert 'Token is alive' in self.response.text, 'Token is dead'
        assert payload.get('name') in self.response.text, 'User is not correct'
