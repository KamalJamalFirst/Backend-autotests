from ..configs.host_configs import API_HOSTS
from ..helpers.validate_code_responses import successful_status_in_response_post_newuser
from ..helpers.validate_data_in_responses import PostNewUserDataValidator
from ..helpers.validate_data_type_in_responses import PostNewUserDataTypeValidator
from requests_oauthlib import OAuth1
import requests
import os
import json


class BackendRequests:

    def __init__(self, payload=None):
        self.environment = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.environment][0]
        self.payload = payload
        self.auth = OAuth1(*API_HOSTS[self.environment][1])



    def post_request(self, headers=None):
        if not headers:
            headers = {'Content-Type': 'application/json'}
        endpoint = '/wp-json/wc/v3/customers'
        rs_post = requests.post(url=f'{self.base_url}{endpoint}', data=json.dumps(self.payload),
                                headers=headers, auth=self.auth)
        successful_status_in_response_post_newuser(rs_post.status_code)
        PostNewUserDataTypeValidator.parse_data(PostNewUserDataTypeValidator, rs_post.json())
        request_data = PostNewUserDataValidator(self.payload)
        updated_payload_with_id = request_data.validate_post_response_create_new_user(rs_post.json())

        return updated_payload_with_id

    def get_request(self):
        pass
