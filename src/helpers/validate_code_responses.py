
def successful_status_in_response_post_newuser(status_code):
    assert status_code in (200, 201), f'Expected status code {200, 201}, but actual {status_code}'


