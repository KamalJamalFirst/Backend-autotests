import os

API_HOSTS = {
    'test': ['http://localhost:8080',
                 [os.environ.get('WC_KEY'), os.environ.get('WC_SECRET')]],
    'dev': '',
    'prod': ''
}


DB_HOSTS = {
    'test': ['localhost',
                 [os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD')]],
    'dev': '',
    'prod': ''
}