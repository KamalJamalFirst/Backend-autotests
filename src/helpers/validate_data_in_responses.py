
class PostNewUserDataValidator:

    def __init__(self, request_data):
        self.request_data = request_data

    def validate_post_response_create_new_user(self, response_from_back):

        for k in self.request_data:
            if k == 'password':
                continue
            else:
                assert self.request_data[k] == response_from_back[k], \
                        f'Value in the request field "{k}" is "{response_from_back[k]}"' \
                        f' BUT must be "{self.request_data[k]}"'
                self.request_data.setdefault('id', response_from_back['id'])
                return self.request_data





