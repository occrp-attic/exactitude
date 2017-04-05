import re
import parsedatetime
from datetime import datetime, date
from normality import stringify

from dalet.validate import format_checker

# JS: '^([12]\\d{3}(-[01]?[1-9](-[0123]?[1-9])?)?)?$'
PARTIAL_DATE_RE = re.compile('^([12]\d{3}(-[01]?[0-9](-[0123]?[0-9])?)?)?$')
CUT_ZEROES = re.compile(r'(\-00?)?\-00?$')


@format_checker.checks('partial-date')
def is_partial_date(date):
    date = stringify(date)
    if date is None:
        return False
    return PARTIAL_DATE_RE.match(date) is not None


def parse_date(text, guess=True, date_format=None):
    """The classic: date parsing, every which way."""
    # handle date/datetime before converting to text.
    if isinstance(text, datetime):
        text = text.date()
    if isinstance(text, date):
        return text.isoformat()

    text = stringify(text)
    if text is None:
        return
    elif date_format is not None:
        # parse with a specified format
        try:
            obj = datetime.strptime(text, date_format)
            return obj.date().isoformat()
        except:
            pass
    elif guess and not is_partial_date(text):
        # use dateparser to guess the format
        try:
            obj = fuzzy_date_parser(text)
            return obj.date().isoformat()
        except Exception:
            pass
    else:
        # limit to the date part of a presumed date string
        text = text[:10]

    # strip -00-00 from dates because it makes ES barf.
    text = CUT_ZEROES.sub('', text)

    if is_partial_date(text):
        return text


def fuzzy_date_parser(text):
    """Thin wrapper around ``parsedatetime`` module.

    Since there's no upstream suppport for multiple locales, this wrapper
    exists.

    :param str text: Text to parse.
    :returns: A parsed date/time object. Raises exception on failure.
    :rtype: datetime
    """
    locales = parsedatetime._locales[:]

    # Loop through all the locales and try to parse successfully our string
    for locale in locales:
        const = parsedatetime.Constants(locale)
        const.re_option += re.UNICODE
        parser = parsedatetime.Calendar(const)
        try:
            parsed, ok = parser.parse(text)
        except:
            continue

        if ok:
            return datetime(*parsed[:6])

    raise Exception('Failed to parse the string.')
