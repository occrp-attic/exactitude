from flanker.addresslib import address


def parse_email(email):
    """Parse and normalize an email address.

    Returns None if this is not an email address.
    """
    if email is not None:
        parsed = address.parse(email)
        if parsed is not None:
            email = parsed.address.lower()
            email = email.strip("'").strip('"')
            return email
