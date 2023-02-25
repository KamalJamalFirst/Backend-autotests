from ..src.utilities.generic_random_user import generate_random_user_credentials_for_registration
from ..src.utilities.backend_requests import BackendRequests
from ..src.dao.customers_dao import CustomersDAO
from loguru import logger
import pytest

logger.add('logs/debug_{time}.log', format='{time}|{level}:\n{message}', level='DEBUG')
@pytest.mark.tcid1
def test_create_user_with_email_and_password():
    """
    Here we are register new user on Website
    """
    payload = generate_random_user_credentials_for_registration()
    api_call = BackendRequests(payload)
    inf_for_db = api_call.post_request()
    check_db_after_request = CustomersDAO(inf_for_db)
    check_db_after_request.check_created_new_customer_in_db()


# @pytest.mark.tcid3
# def test_create_user_with_existing_email():
#     pass
