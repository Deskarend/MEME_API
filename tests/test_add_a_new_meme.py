import allure
import pytest

from helper import MemePayload


class TestAddNewMem:
    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check successful adding meme')
    def test_add_a_new_meme(
            self, add_a_new_meme_endpoint, payload_for_new_meme, authorize_token, payload_for_authorization
    ):
        add_a_new_meme_endpoint.add_a_new_mem(payload_for_new_meme, authorize_token)

        add_a_new_meme_endpoint.check_response_of_successful_adding_meme(
            payload_for_new_meme, payload_for_authorization
        )

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme without authorization')
    def test_add_a_new_meme_without_token(self, add_a_new_meme_endpoint, payload_for_new_meme):
        add_a_new_meme_endpoint.add_a_new_mem(payload_for_new_meme)

        add_a_new_meme_endpoint.check_status_code_is_401()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with authorization')
    def test_add_a_new_meme_with_incorrect_token(self, add_a_new_meme_endpoint, payload_for_new_meme):
        incorrect_token = 'incorrect_token'
        add_a_new_meme_endpoint.add_a_new_mem(payload_for_new_meme, incorrect_token)

        add_a_new_meme_endpoint.check_status_code_is_401()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme without required field')
    @pytest.mark.parametrize('payload', [
        MemePayload().payloads_without_text, MemePayload().payloads_without_url,
        MemePayload().payloads_without_tags, MemePayload().payloads_without_info
    ])
    def test_add_a_new_meme_without_required_field(self, add_a_new_meme_endpoint, payload, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with empty payload')
    def test_add_a_new_meme_with_empty_payload(self, add_a_new_meme_endpoint, authorize_token):
        payload = {}
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme without payload')
    def test_add_a_new_meme_without_payload(self, add_a_new_meme_endpoint, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload=None, token=authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with empty text field')
    @pytest.mark.parametrize('payload', MemePayload().payloads_with_empty_text)
    def test_add_a_new_meme_with_empty_text_field(self, add_a_new_meme_endpoint, payload, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with empty url field')
    @pytest.mark.parametrize('payload', MemePayload().payloads_with_empty_url)
    def test_add_a_new_meme_with_empty_url_field(self, add_a_new_meme_endpoint, payload, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with empty tags field')
    @pytest.mark.parametrize('payload', MemePayload().payloads_with_empty_tags)
    def test_add_a_new_meme_with_empty_tags_field(self, add_a_new_meme_endpoint, payload, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with empty info field')
    @pytest.mark.parametrize('payload', MemePayload().payloads_with_empty_info)
    def test_add_a_new_meme_with_empty_info_field(self, add_a_new_meme_endpoint, payload, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with incorrect text field')
    @pytest.mark.parametrize('payload', MemePayload().payloads_with_incorrect_text)
    def test_add_a_new_meme_with_incorrect_text_field(self, add_a_new_meme_endpoint, payload, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with incorrect url field')
    @pytest.mark.parametrize('payload', MemePayload().payloads_with_incorrect_url)
    def test_add_a_new_meme_with_incorrect_url_field(self, add_a_new_meme_endpoint, payload, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with incorrect tags field')
    @pytest.mark.parametrize('payload', MemePayload().payloads_with_incorrect_tags)
    def test_add_a_new_meme_with_incorrect_tags_field(self, add_a_new_meme_endpoint, payload, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()

    @allure.tag('POSTs')
    @allure.story('Add a mem')
    @allure.title('Check adding meme with incorrect info field')
    @pytest.mark.parametrize('payload', MemePayload().payloads_with_incorrect_info)
    def test_add_a_new_meme_with_incorrect_info_field(self, add_a_new_meme_endpoint, payload, authorize_token):
        add_a_new_meme_endpoint.add_a_new_mem(payload, authorize_token)

        add_a_new_meme_endpoint.check_status_code_is_400()
