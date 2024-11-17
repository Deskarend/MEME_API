import random

from faker import Faker

from data import tags
from endpoints.authorize_endpoint import AuthorizeEndpointEndpoint
from endpoints.get_all_memes import GetAllMemesEndpoint


fake = Faker()

not_existing_ids = [random.randint(1000000, 999999999), 'NotExistingId']


def generate_meme_payload():
    payload = {
        "text": fake.text(),
        "url": fake.url(),
        "tags": [random.choice(tags) for _ in range(random.randrange(2, len(tags)))],
        "info": {
            "colors": [fake.color() for _ in range(1, random.randrange(2, 5))],
            "objects": [fake.country() for _ in range(1, random.randrange(2, 5))]
        }
    }
    return payload


def get_empty_field_payload(payload, field):
    empty_field = []
    for empty in [None, '', [], {}]:
        new_payload = payload.copy()
        new_payload[field] = empty
        empty_field.append(new_payload)
    return empty_field


def delete_the_field_in_payload(payload, field):
    new_payload = payload.copy()
    del new_payload[field]
    return new_payload


def get_incorrect_field_payloads(payload, field, data_type):
    new_payload = payload.copy()
    data_types = {
        "string": fake.name(),
        "digit": fake.random_digit() + 1,
        "float": (fake.random_digit() + 1) / 1,
        "array": [fake.name(), fake.last_name()],
        "object": {'name': fake.name(), 'l_n': fake.last_name()},
        "bools": fake.boolean()
    }

    incorrect_field_payloads = []
    for a_type in data_types:
        if data_type != a_type:
            incorrect_field_payload = new_payload.copy()

            new_value = data_types[a_type]
            incorrect_field_payload[field] = new_value

            incorrect_field_payloads.append(incorrect_field_payload)

    return incorrect_field_payloads


class IncorrectAuthorizationPayload:
    payload = {'name': fake.name()}

    payload_with_empty_name = get_empty_field_payload(payload, 'name')
    payload_with_incorrect_name = get_incorrect_field_payloads(payload, 'name', 'string')


class AllMemes:
    all_memes = GetAllMemesEndpoint()
    authorize = AuthorizeEndpointEndpoint()

    authorize.authorize({"name": "Admin)"})
    authorize_token = authorize.get_authorization_token()
    all_memes.get_all_memes(authorize_token)

    all_memes = all_memes.response_json.get('data')
    all_meme_ids = [mem.get('id') for mem in all_memes]


class MemePayload:
    payload = None

    payloads_without_text = None
    payloads_without_url = None
    payloads_without_tags = None
    payloads_without_info = None

    payloads_with_empty_text = None
    payloads_with_empty_url = None
    payloads_with_empty_tags = None
    payloads_with_empty_info = None

    payloads_with_incorrect_text = None
    payloads_with_incorrect_url = None
    payloads_with_incorrect_tags = None
    payloads_with_incorrect_info = None

    def __init__(self):
        self.payload = generate_meme_payload()
        self.generate_all_payloads()

    def generate_payloads_without_field(self):
        self.payloads_without_text = delete_the_field_in_payload(self.payload, 'text')
        self.payloads_without_url = delete_the_field_in_payload(self.payload, 'url')
        self.payloads_without_tags = delete_the_field_in_payload(self.payload, 'tags')
        self.payloads_without_info = delete_the_field_in_payload(self.payload, 'info')

    def generate_payloads_with_empty_field(self):
        self.payloads_with_empty_text = get_empty_field_payload(self.payload, 'text')
        self.payloads_with_empty_url = get_empty_field_payload(self.payload, 'url')
        self.payloads_with_empty_tags = get_empty_field_payload(self.payload, 'tags')
        self.payloads_with_empty_info = get_empty_field_payload(self.payload, 'info')

    def generate_payloads_with_incorrect_field(self):
        self.payloads_with_incorrect_text = get_incorrect_field_payloads(self.payload, 'text', 'string')
        self.payloads_with_incorrect_url = get_incorrect_field_payloads(self.payload, 'url', 'string')
        self.payloads_with_incorrect_tags = get_incorrect_field_payloads(self.payload, 'tags', 'array')
        self.payloads_with_incorrect_info = get_incorrect_field_payloads(self.payload, 'info', 'object')

    def generate_all_payloads(self):
        self.generate_payloads_without_field()
        self.generate_payloads_with_empty_field()
        self.generate_payloads_with_incorrect_field()


class EditMemePayload(MemePayload):
    payloads_without_id = None
    payloads_with_empty_id = None
    payloads_with_incorrect_id = None

    def __init__(self, meme_id=1):
        self.payload = generate_meme_payload()
        self.payload.update({"id": meme_id})
        self.generate_all_payloads()

    def generate_all_payloads(self):
        super().generate_all_payloads()
        self.payloads_without_id = delete_the_field_in_payload(self.payload, 'id')
        self.payloads_with_empty_id = get_empty_field_payload(self.payload, 'id')
        self.payloads_with_incorrect_id = get_incorrect_field_payloads(self.payload, 'id', 'digit')
