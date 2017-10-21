from pycountry import languages

LANGUAGE_NAMES = {l.alpha_2: l.name for l in languages}


def is_language_code(code):
    if code is None:
        return False
    return code.lower() in LANGUAGE_NAMES.keys()
