def build_profile(first, last, **user_info): # Often see parameter name **kwargs used to collect non-specific keyword arguments.
    """ Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info