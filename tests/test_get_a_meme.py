import allure
import pytest

import helper


class TestGetMeme:

    @allure.tag('GETs')
    @allure.story('Get a meme')
    @allure.title('Check getting only one meme')
    def test_get_a_meme(self, get_a_meme_endpoint, random_mem_id, authorize_token):
        get_a_meme_endpoint.get_a_meme(random_mem_id, authorize_token)

        get_a_meme_endpoint.check_response_getting_a_mem()

    @allure.tag('GETs')
    @allure.story('Get a meme')
    @allure.title('Check getting only one meme without authorization')
    def test_get_a_meme_without_token(self, get_a_meme_endpoint, random_mem_id):
        get_a_meme_endpoint.get_a_meme(random_mem_id)

        get_a_meme_endpoint.check_status_code_is_401()

    @allure.tag('GETs')
    @allure.story('Get a meme')
    @allure.title('Check getting not existing meme')
    @pytest.mark.parametrize('not_existing_id', helper.not_existing_ids)
    def test_get_a_not_existing_meme(self, get_a_meme_endpoint, authorize_token, not_existing_id):
        get_a_meme_endpoint.get_a_meme(not_existing_id, authorize_token)

        get_a_meme_endpoint.check_status_code_is_404()

    @allure.tag('GETs')
    @allure.story('Get a meme')
    @allure.title('Check getting meme with incorrect token')
    def test_get_a_meme_with_incorrect_token(self, get_a_meme_endpoint, random_mem_id):
        not_existing_token = 'not_existing_token'
        get_a_meme_endpoint.get_a_meme(random_mem_id, not_existing_token)

        get_a_meme_endpoint.check_status_code_is_401()
