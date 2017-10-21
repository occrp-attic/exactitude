from normality import stringify


def parse_email(email):
    """Parse and normalize an email address.

    Returns None if this is not an email address.
    """
    email = stringify(email)
    if email is None:
        return
    if '@' not in email:
        return
    return email
    # parsed = address.parse(email)
    # if parsed is not None:
    #     email = parsed.address.lower()
    #     email = email.strip("'").strip('"')
    #     return email
