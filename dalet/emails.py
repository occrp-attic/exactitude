from normality import stringify
from flanker.addresslib import address


def parse_email(email):
    """Parse and normalize an email address.

    Returns None if this is not an email address.
    """
    email = stringify(email)
    if email is None:
        return
    parsed = address.parse(email)
    if parsed is not None:
        email = parsed.address.lower()
        email = email.strip("'").strip('"')
        return email
