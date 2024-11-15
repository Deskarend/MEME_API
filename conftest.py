import random

import pytest
from faker import Faker

from endpoints.add_a_new_meme import AddNewMemEndpoint
from endpoints.authorize_endpoint import AuthorizeEndpointEndpoint
from endpoints.check_token_endpoint import CheckTokenEndpoint
from endpoints.delete_meme_endpoint import DeleteMemeEndpoint
from endpoints.edit_meme_endpoint import EditMemeEndpoint
from endpoints.get_a_mem import GetMemEndpoint
from endpoints.get_all_memes import GetAllMemesEndpoint
from helper import AllMemes, MemePayload, EditMemePayload

fake = Faker()


@pytest.fixture
def authorize_endpoint():
    return AuthorizeEndpointEndpoint()


@pytest.fixture
def check_token_endpoint():
    return CheckTokenEndpoint()


@pytest.fixture
def get_all_memes_endpoint():
    return GetAllMemesEndpoint()


@pytest.fixture
def get_a_meme_endpoint():
    return GetMemEndpoint()


@pytest.fixture
def add_a_new_meme_endpoint():
    return AddNewMemEndpoint()


@pytest.fixture
def edit_meme_endpoint():
    return EditMemeEndpoint()


@pytest.fixture
def delete_meme_endpoint():
    return DeleteMemeEndpoint()


@pytest.fixture
def payload_for_authorization():
    return {
        'name': fake.name()
    }


@pytest.fixture
def not_meme_owner_payload_for_authorization():
    return {
        'name': fake.name()
    }


@pytest.fixture
def authorize_token(authorize_endpoint, payload_for_authorization):
    authorize_endpoint.authorize(payload_for_authorization)
    token = authorize_endpoint.get_authorization_token()
    return token


@pytest.fixture
def not_meme_owner_authorize_token(authorize_endpoint, not_meme_owner_payload_for_authorization):
    authorize_endpoint.authorize(not_meme_owner_payload_for_authorization)
    token = authorize_endpoint.get_authorization_token()
    return token


@pytest.fixture
def new_meme_id(add_a_new_meme_endpoint, payload_for_new_meme, authorize_token):
    add_a_new_meme_endpoint.add_a_new_mem(payload_for_new_meme, authorize_token)
    new_meme_id = add_a_new_meme_endpoint.get_mem_id()
    return new_meme_id


@pytest.fixture
def payload_for_new_meme():
    return MemePayload().payload


@pytest.fixture
def payload_for_edit_meme(new_meme_id):
    return EditMemePayload(new_meme_id).payload


@pytest.fixture
def meme_ids():
    return AllMemes.all_meme_ids


@pytest.fixture
def random_mem_id(meme_ids):
    random_mem_id = random.choice(meme_ids)
    return random_mem_id
