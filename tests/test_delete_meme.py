import allure
import pytest

import helper


class TestDeleteMeme:
    @allure.tag('DELETEs')
    @allure.story('Delete the meme')
    @allure.title('Check successful deleting meme')
    def test_delete_meme(self, delete_meme_endpoint, new_meme_id, authorize_token, get_a_meme_endpoint):
        delete_meme_endpoint.delete_the_meme(new_meme_id, authorize_token)
        delete_meme_endpoint.check_response_of_successful_deleted_meme(new_meme_id)

        get_a_meme_endpoint.get_a_meme(new_meme_id, authorize_token)
        get_a_meme_endpoint.check_status_code_is_404()

    @allure.tag('DELETEs')
    @allure.story('Delete the meme')
    @allure.title('Check deleting meme without authorization')
    def test_delete_meme_without_authorization(self, delete_meme_endpoint, new_meme_id):
        delete_meme_endpoint.delete_the_meme(new_meme_id)

        delete_meme_endpoint.check_status_code_is_401()

    @allure.tag('DELETEs')
    @allure.story('Delete the meme')
    @allure.title('Check deleting meme with incorrect authorization')
    def test_delete_meme_with_incorrect_authorization(self, delete_meme_endpoint, new_meme_id):
        incorrect_token = 'incorrect_token'
        delete_meme_endpoint.delete_the_meme(new_meme_id, incorrect_token)

        delete_meme_endpoint.check_status_code_is_401()

    @allure.tag('DELETEs')
    @allure.story('Delete the meme')
    @allure.title('Check deleting meme without authorization')
    @pytest.mark.parametrize('not_existing_id', helper.not_existing_ids)
    def test_delete_not_existing_meme(self, delete_meme_endpoint, authorize_token, not_existing_id):
        delete_meme_endpoint.delete_the_meme(not_existing_id, authorize_token)

        delete_meme_endpoint.check_status_code_is_404()

    @allure.tag('DELETEs')
    @allure.story('Delete the meme')
    @allure.title('Check deleting meme without meme owner')
    def test_delete_meme_without_meme_owner(self, delete_meme_endpoint, new_meme_id, not_meme_owner_authorize_token):
        delete_meme_endpoint.delete_the_meme(new_meme_id, not_meme_owner_authorize_token)

        delete_meme_endpoint.check_status_code_is_403()

    @allure.tag('DELETEs')
    @allure.story('Delete the same meme twice')
    @allure.title('Check successful deleting meme')
    def test_delete_the_same_meme_twice(self, delete_meme_endpoint, new_meme_id, authorize_token):
        delete_meme_endpoint.delete_the_meme(new_meme_id, authorize_token)
        delete_meme_endpoint.delete_the_meme(new_meme_id, authorize_token)

        delete_meme_endpoint.check_status_code_is_404()
