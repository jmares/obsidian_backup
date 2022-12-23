def get_password(salt):
    """
    Create a password
    """
    password = ""
    # give password a value based on a static string or formula
    # with a formula you can even give each compressed vault a different password
    # example:
    password = "#" + salt + "!"
    return password