import allure


class BaseEndpoint:
    response = None
    response_json = None
    BASE_URL = 'http://167.172.172.115:52355'

    def _check_status_code(self, status_code):
        assert self.response.status_code == status_code, (f'Expected status code is {status_code}, '
                                                          f'Actual is {self.response.status_code}')

    @allure.step('Check that status code is 200')
    def check_status_code_is_200(self):
        self._check_status_code(200)

    @allure.step('Check that status code is 400')
    def check_status_code_is_400(self):
        self._check_status_code(400)

    @allure.step('Check that status code is 401')
    def check_status_code_is_401(self):
        self._check_status_code(401)

    @allure.step('Check that status code is 403')
    def check_status_code_is_403(self):
        self._check_status_code(403)

    @allure.step('Check that status code is 404')
    def check_status_code_is_404(self):
        self._check_status_code(404)
