
from ..helpers.connect_db import create_connection_with_db

class CustomersDAO:

    def __init__(self, inf_for_db):
        self.inf_for_db = inf_for_db

    def check_created_new_customer_in_db(self):
        sql = f'SELECT * FROM wordpress_db.wp_users WHERE ID="{self.inf_for_db["id"]}"' \
              f' and user_email="{self.inf_for_db["email"]}"' \
              f' and user_login="{self.inf_for_db["username"]}";'
        connect = create_connection_with_db(sql)
        return connect
