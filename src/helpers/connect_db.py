import pymysql, os
from pymysql import cursors
from ..configs.host_configs import DB_HOSTS


def create_connection_with_db(sql):
    env = os.environ.get('ENV', 'test')
    create_connection_with_db = pymysql.connect(host=DB_HOSTS[env][0],
                                                user=DB_HOSTS[env][1][0], password=DB_HOSTS[env][1][1],
                                                database='wordpress_db', port=3306)
    try:
        cur = create_connection_with_db.cursor(cursors.DictCursor)
        cur.execute(sql)
        rs_dict = cur.fetchall()
        cur.close()
    except Exception as e:
            raise Exception('Failed running sql \n'
                            f'Error: {str(e)}')
    finally:
        create_connection_with_db.close()

    return rs_dict