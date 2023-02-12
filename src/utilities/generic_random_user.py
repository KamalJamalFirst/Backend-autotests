from faker import Faker


def generate_random_user_credentials_for_registration(domain=None, email_prefix=None, first_name=None,
                                                      last_name=None, username=None, password=None, **kwargs):
    """
    Here we generate random user credentials to register new user
    """
    user_credentials = {'email': f'{email_prefix}@{domain}',
                        'first_name': first_name,
                        'last_name': last_name,
                        'username': username,
                        'password': password
                        }

    check_user_credentials = {'email': Faker().email(),
                              'first_name': (fn := Faker().first_name()),
                              'last_name': (ln := Faker().last_name()),
                              'username': f'{fn}_{ln}',
                              'password': Faker().password(
                                  length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
                              }

    for check in user_credentials:
        if check == 'email':
            if (email_prefix and domain) == None:
                user_credentials['email'] = check_user_credentials['email']
            elif email_prefix == None:
                user_credentials['email'] = check_user_credentials['email'][:check_user_credentials['email'].find('@')] \
                                        + domain
            elif domain == None:
                user_credentials['email'] = \
                    email_prefix + check_user_credentials['email'][check_user_credentials['email'].find('@'):]
            else:
                continue
        else:
            if user_credentials[check] == None:
                user_credentials[check] = check_user_credentials[check]

    user_credentials.update(kwargs)

    return user_credentials


