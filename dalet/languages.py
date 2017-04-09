from babel import Locale

LANGUAGE_NAMES = dict(Locale('en').languages.items())
LANGUAGE_NAMES = {k: v for k, v in LANGUAGE_NAMES.items() if len(k) == 2}


def is_language_code(code):
    if code is None:
        return False
    return code.lower() in LANGUAGE_NAMES.keys()
