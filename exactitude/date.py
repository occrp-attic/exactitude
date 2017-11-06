import re
import parsedatetime
from normality import stringify
from datetime import datetime, date

from exactitude.common import ExactitudeType


class DateType(ExactitudeType):
    # JS: '^([12]\\d{3}(-[01]?[1-9](-[0123]?[1-9])?)?)?$'
    PARTIAL_DATE_RE = re.compile('^([12]\d{3}(-[01]?[0-9](-[0123]?[0-9])?)?)?$')
    CUT_ZEROES = re.compile(r'(\-00?)?\-00?$')

    def validate(self, obj, **kwargs):
        """Check if a thing is a valid date."""
        obj = stringify(obj)
        if obj is None:
            return False
        return self.PARTIAL_DATE_RE.match(obj) is not None

    def clean(self, text, guess=True, format=None, **kwargs):
        """The classic: date parsing, every which way."""
        # handle date/datetime before converting to text.
        if isinstance(text, datetime):
            text = text.date()
        if isinstance(text, date):
            return text.isoformat()

        text = stringify(text)
        if text is None:
            return

        if format is not None:
            # parse with a specified format
            try:
                obj = datetime.strptime(text, format)
                return obj.date().isoformat()
            except:
                return None

        if guess and not self.validate(text):
            # use dateparser to guess the format
            try:
                obj = self.fuzzy_date_parser(text)
                return obj.date().isoformat()
            except Exception:
                pass
        else:
            # limit to the date part of a presumed date string
            text = text[:10]

        # strip -00-00 from dates because it makes ES barf.
        text = self.CUT_ZEROES.sub('', text)

        if self.validate(text):
            return text

    def fuzzy_date_parser(self, text):
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
