import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class AddNewMemEndpoint(BaseEndpoint):
    @allure.step('Add a new meme')
    def add_a_new_mem(self, payload, token=None):
        headers = {"Authorization": token}
        self.response = requests.post(f'{self.BASE_URL}/meme', json=payload, headers=headers)
        if self.response.status_code == 200:
            self.response_json = self.response.json()

    @allure.step('Get a new meme id')
    def get_mem_id(self):
        return self.response_json.get('id')

    @allure.step('Check response of successful added meme')
    def check_response_of_successful_adding_meme(self, meme_payload, authorize_payload):
        self.check_status_code_is_200()
        assert self.response_json.get('text') == meme_payload.get('text'), 'Added meme text is incorrect'
        assert self.response_json.get('url') == meme_payload.get('url'), 'Added meme url is incorrect'
        assert self.response_json.get('tags') == meme_payload.get('tags'), 'Added meme tags is incorrect'
        assert self.response_json.get('info') == meme_payload.get('info'), 'Added meme info is incorrect'
        assert self.response_json.get('updated_by') == authorize_payload.get('name'), 'There is incorrect updater'
        assert self.response_json.get('id'), 'There is no id'
