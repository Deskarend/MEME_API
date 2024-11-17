import allure
import pytest

from helper import IncorrectAuthorizationPayload


class TestAuthorize:
    @allure.tag('POSTs')
    @allure.story('Authorize')
    @allure.title('Check successful authorize')
    def test_successful_authorize(self, authorize_endpoint, payload_for_authorization):
        authorize_endpoint.authorize(payload_for_authorization)

        authorize_endpoint.check_response_of_successful_authorize(payload_for_authorization)

    @allure.tag('POSTs')
    @allure.story('Authorize')
    @allure.title('Check authorize with incorrect meme_payload')
    @pytest.mark.parametrize('payload', IncorrectAuthorizationPayload.payload_with_incorrect_name)
    def test_authorize_with_incorrect_payload(self, authorize_endpoint, payload):
        authorize_endpoint.authorize(payload)

        authorize_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Authorize')
    @allure.title('Check authorize with empty name')
    @pytest.mark.parametrize('payload', IncorrectAuthorizationPayload.payload_with_empty_name)
    def test_authorize_with_empty_name(self, authorize_endpoint, payload):
        authorize_endpoint.authorize(payload)

        authorize_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Authorize')
    @allure.title('Check authorize with empty meme_payload')
    def test_authorize_with_empty_payload(self, authorize_endpoint):
        payload = {}
        authorize_endpoint.authorize(payload)

        authorize_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Authorize')
    @allure.title('Check authorize without meme_payload')
    def test_authorize_without_payload(self, authorize_endpoint):
        authorize_endpoint.authorize()

        authorize_endpoint.check_status_code_is_400()
