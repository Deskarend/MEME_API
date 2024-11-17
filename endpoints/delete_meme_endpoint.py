import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class DeleteMemeEndpoint(BaseEndpoint):
    @allure.step('Delete the meme')
    def delete_the_meme(self, mem_id, token=None):
        headers = {'Authorization': token}
        self.response = requests.delete(f'{self.BASE_URL}/meme/{mem_id}', headers=headers)

    @allure.step('Check response of successful deleted meme')
    def check_response_of_successful_deleted_meme(self, mem_id):
        self.check_status_code_is_200()
        assert f"Meme with id {mem_id} successfully deleted" in self.response.text
