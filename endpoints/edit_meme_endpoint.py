import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class EditMemeEndpoint(BaseEndpoint):
    @allure.step('Edit the meme')
    def edit_meme(self, token, meme_id, payload):
        headers = {"Authorization": token}
        self.response = requests.put(f'{self.BASE_URL}/meme/{meme_id}', json=payload, headers=headers)
        if self.response.status_code == 200:
            self.response_json = self.response.json()

    @allure.step('Check response of successful edited meme')
    def check_response_of_successful_edited_meme(self, meme_payload, meme_id, authorize_payload):
        self.check_status_code_is_200()
        assert self.response_json.get('text') == meme_payload.get('text'), 'Edited meme text is incorrect'
        assert self.response_json.get('url') == meme_payload.get('url'), 'Edited meme url is incorrect'
        assert self.response_json.get('tags') == meme_payload.get('tags'), 'Edited meme tags is incorrect'
        assert self.response_json.get('info') == meme_payload.get('info'), 'Edited meme info is incorrect'
        assert self.response_json.get('updated_by') == authorize_payload.get('name'), 'There is incorrect updater'
        assert self.response_json.get('id') == str(meme_id), 'Id is incorrect'
