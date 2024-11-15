import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class GetAllMemesEndpoint(BaseEndpoint):
    @allure.step('Get all memes')
    def get_all_memes(self, token=None):
        headers = {'Authorization': token}
        self.response = requests.get(f'{self.BASE_URL}/meme', headers=headers)
        if self.response.status_code == 200:
            self.response_json = self.response.json()

    @allure.step('Check response successful getting all memes')
    def check_response_getting_all_memes(self):
        self.check_status_code_is_200()
        assert len(self.response_json.get('data')) > 1, 'There are less two memes in all memes'
