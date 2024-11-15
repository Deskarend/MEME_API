import allure
import pytest

import helper
from helper import EditMemePayload


class TestEditMeme:
    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check successful editing meme')
    def test_edit_the_meme(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload_for_authorization
    ):
        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_response_of_successful_edited_meme(
            payload_for_edit_meme, new_meme_id, payload_for_authorization
        )

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme without authorization')
    def test_edit_the_meme_without_authorization(
            self, edit_meme_endpoint, new_meme_id, payload_for_edit_meme, payload_for_authorization
    ):
        edit_meme_endpoint.edit_meme(token=None, meme_id=new_meme_id, payload=payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_401()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with incorrect authorization')
    def test_edit_the_meme_with_incorrect_authorization(
            self, edit_meme_endpoint, new_meme_id, payload_for_edit_meme, payload_for_authorization
    ):
        incorrect_token = 'incorrect_token'
        edit_meme_endpoint.edit_meme(incorrect_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_401()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme without required field')
    @pytest.mark.parametrize('payload',
                             ['payloads_without_id',
                              'payloads_without_text',
                              'payloads_without_url',
                              'payloads_without_tags',
                              'payloads_with_empty_tags'])
    def test_edit_the_meme_without_required_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, getattr(EditMemePayload(new_meme_id), payload))

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with empty payload')
    def test_edit_the_meme_with_empty_payload(self, edit_meme_endpoint, authorize_token, new_meme_id):
        payload = {}

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme without payload')
    def test_edit_the_meme_without_payload(self, edit_meme_endpoint, authorize_token, new_meme_id):
        edit_meme_endpoint.edit_meme(token=authorize_token, meme_id=new_meme_id, payload=None)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with empty id field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_empty_id)
    def test_edit_the_meme_with_empty_id_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload):
        payload_for_edit_meme['id'] = payload

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with empty text field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_empty_text)
    def test_edit_the_meme_with_empty_text_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        payload_for_edit_meme['text'] = payload

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with empty url field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_empty_url)
    def test_edit_the_meme_with_empty_url_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        payload_for_edit_meme['url'] = payload

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with empty tags field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_empty_tags)
    def test_edit_the_meme_with_empty_tags_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        payload_for_edit_meme['tags'] = payload

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with empty info field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_empty_info)
    def test_edit_the_meme_with_empty_info_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        payload_for_edit_meme['info'] = payload['info']

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with incorrect id field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_incorrect_id)
    def test_edit_the_meme_with_incorrect_id_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        payload_for_edit_meme['id'] = payload

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with incorrect text field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_incorrect_text)
    def test_edit_the_meme_with_incorrect_text_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        payload_for_edit_meme['text'] = payload

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with incorrect url field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_incorrect_url)
    def test_edit_the_meme_with_incorrect_url_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        payload_for_edit_meme['url'] = payload

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with incorrect tags field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_incorrect_tags)
    def test_edit_the_meme_with_incorrect_tags_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        payload_for_edit_meme['tags'] = payload

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with incorrect info field')
    @pytest.mark.parametrize('payload', EditMemePayload().payloads_with_incorrect_info)
    def test_edit_the_meme_with_incorrect_info_field(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, payload
    ):
        payload_for_edit_meme['info'] = payload['info']

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with different ids in body and query (new id is in query)')
    def test_edit_the_meme_with_new_id_in_query(
            self, add_a_new_meme_endpoint, payload_for_new_meme, edit_meme_endpoint, authorize_token, new_meme_id,
            payload_for_edit_meme
    ):
        add_a_new_meme_endpoint.add_a_new_mem(payload_for_new_meme, authorize_token)
        another_id = add_a_new_meme_endpoint.get_mem_id()

        edit_meme_endpoint.edit_meme(authorize_token, another_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with different ids in body and query (new id is in body)')
    def test_edit_the_meme_with_new_id_in_body(
            self, add_a_new_meme_endpoint, payload_for_new_meme, edit_meme_endpoint, authorize_token, new_meme_id,
            payload_for_edit_meme
    ):
        add_a_new_meme_endpoint.add_a_new_mem(payload_for_new_meme, authorize_token)
        another_id = add_a_new_meme_endpoint.get_mem_id()

        payload_for_edit_meme['id'] = int(another_id)

        edit_meme_endpoint.edit_meme(authorize_token, new_meme_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_400()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme with not existing id')
    @pytest.mark.parametrize('not_existing_id', helper.not_existing_ids)
    def test_edit_the_meme_with_not_existing_id(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, not_existing_id
    ):
        edit_meme_endpoint.edit_meme(authorize_token, not_existing_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_404()

    @allure.tag('PUTs')
    @allure.story('Edit the mem')
    @allure.title('Check editing meme without meme owner')
    def test_edit_the_meme_without_meme_owner(
            self, edit_meme_endpoint, authorize_token, new_meme_id, payload_for_edit_meme, random_mem_id
    ):
        payload_for_edit_meme['id'] = random_mem_id
        edit_meme_endpoint.edit_meme(authorize_token, random_mem_id, payload_for_edit_meme)

        edit_meme_endpoint.check_status_code_is_403()
