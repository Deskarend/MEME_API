import allure


class TestGetAllMemes:

    @allure.tag('GETs')
    @allure.story('Get all memes')
    @allure.title('Check getting all memes')
    def test_get_all_memes(self, get_all_memes_endpoint, authorize_token):
        get_all_memes_endpoint.get_all_memes(authorize_token)

        get_all_memes_endpoint.check_response_getting_all_memes()

    @allure.tag('GETs')
    @allure.story('Get all memes')
    @allure.title('Check getting all memes without authorization')
    def test_get_all_memes_without_token(self, get_all_memes_endpoint):
        get_all_memes_endpoint.get_all_memes()

        get_all_memes_endpoint.check_status_code_is_401()

    @allure.tag('GETs')
    @allure.story('Get all memes')
    @allure.title('Check getting all memes with incorrect authorization')
    def test_get_all_memes_with_incorrect_token(self, get_all_memes_endpoint):
        not_existing_token = 'not_existing_token'
        get_all_memes_endpoint.get_all_memes(not_existing_token)

        get_all_memes_endpoint.check_status_code_is_401()
