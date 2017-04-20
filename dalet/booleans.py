from normality import stringify

BOOL_TRUEISH = ['1', 'yes', 'y', 't', 'true', 'enabled']


def parse_boolean(text, default=False):
    text = stringify(text)
    if text is None:
        return default
    text = text.strip().lower()
    return text in BOOL_TRUEISH
