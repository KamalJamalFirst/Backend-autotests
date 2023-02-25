from loguru import logger
from ..helpers.connect_db import create_connection_with_db

class CustomersDAO:

    def __init__(self, inf_for_db):
        self.inf_for_db = inf_for_db


    def check_created_new_customer_in_db(self):
        logger.info(f'New user will be checked in DB by SQL select with credentials id={self.inf_for_db["id"]}, '
                    f'email={self.inf_for_db["email"]}, username={self.inf_for_db["username"]}')
        sql = f'SELECT * FROM wordpress_db.wp_users WHERE ID="{self.inf_for_db["id"]}"' \
              f' and user_email="{self.inf_for_db["email"]}"' \
              f' and user_login="{self.inf_for_db["username"]}";'
        logger.debug('Start connection with DB and executing SQL select')
        connect = create_connection_with_db(sql)
        logger.debug('Connection with DB and executing SQL select successfully passed. New user was found in DB')
        return connect
