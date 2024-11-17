import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class GetMemEndpoint(BaseEndpoint):
    @allure.step('Get a meme')
    def get_a_meme(self, mem_id, token=None):
        headers = {'Authorization': token}
        self.response = requests.get(f'{self.BASE_URL}/meme/{mem_id}', headers=headers)
        if self.response.status_code == 200:
            self.response_json = self.response.json()

    @allure.step('Check response successful getting a meme')
    def check_response_getting_a_mem(self, mem_id):
        self.check_status_code_is_200()

        assert self.response_json.get('id') == mem_id, 'Mem has incorrect id'
        assert self.response_json.get('text'), 'Mem has not text'
        assert self.response_json.get('url'), 'Mem has not url'
        assert self.response_json.get('tags'), 'Mem has not url'
        assert self.response_json.get('info'), 'Mem has not info'
