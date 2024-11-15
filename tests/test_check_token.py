import allure


class TestCheckToken:
    @allure.tag('GETs')
    @allure.story('Check token')
    @allure.title('Check successful check token request with alive token')
    def test_successful_check_token_with_alive_token(
            self, check_token_endpoint, authorize_token, payload_for_authorization
    ):
        check_token_endpoint.check_token(authorize_token)

        check_token_endpoint.check_response_of_successful_check_token(payload_for_authorization)

    @allure.tag('GETs')
    @allure.story('Check token')
    @allure.title('Check "check token" request with not alive token')
    def test_successful_check_token_with_not_existing_token(self, check_token_endpoint):
        not_existing_token = 'not_existing_token'
        check_token_endpoint.check_token(not_existing_token)

        check_token_endpoint.check_status_code_is_404()
