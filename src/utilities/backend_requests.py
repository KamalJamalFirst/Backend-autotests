from ..configs.host_configs import API_HOSTS
from ..helpers.validate_code_responses import successful_status_in_response
from ..helpers.validate_data_in_responses import PostNewUserDataValidator
from ..helpers.validate_data_type_in_responses import parse_data
from requests_oauthlib import OAuth1
from loguru import logger
import requests
import os
import json


class BackendRequests:

    def __init__(self, payload=None):
        self.environment = os.getenv('ENV', 'test')
        self.base_url = API_HOSTS[self.environment][0]
        self.payload = payload
        self.auth = OAuth1(*API_HOSTS[self.environment][1])

    def post_request(self, headers=None):
        if not headers:
            headers = {'Content-Type': 'application/json'}
        endpoint = '/wp-json/wc/v3/customers'
        logger.debug(f'Start sending POST request to {self.base_url}{endpoint} with data {json.dumps(self.payload)}')
        rs_post = requests.post(url=f'{self.base_url}{endpoint}', data=json.dumps(self.payload),
                                headers=headers, auth=self.auth)
        logger.debug(f'Response from back {rs_post.status_code}')
        successful_status_in_response(rs_post.status_code)
        logger.debug(f'Start validating data type in POST request')
        assert parse_data(rs_post.json()), parse_data(rs_post.json())
        logger.debug(f'Validating data type in POST response successfully passed')
        request_data = PostNewUserDataValidator(self.payload)
        logger.debug(f'Compare user data between request and response. Data must be the same')
        updated_payload_with_id = request_data.validate_post_response_create_new_user(rs_post.json())
        logger.debug(f'Comparing user data between request and response successfully passed')
        logger.info('In request data was added new field ID, which was given to user after POST request')
        return updated_payload_with_id

    def get_request(self, payload=None, headers=None):
        if not headers:
            headers = {'Content-Type': 'application/json'}
        endpoint = '/wp-json/wc/v3/customers'
        logger.debug(f'GET Request is sent to {self.base_url}{endpoint} with data {json.dumps(self.payload)}')
        rs_get = requests.get(url=f'{self.base_url}{endpoint}', data=json.dumps(self.payload),
                                headers=headers, auth=self.auth)
        logger.debug(f'Response from back {rs_get.status_code}')
        successful_status_in_response(rs_get.status_code)
        return rs_get.json()