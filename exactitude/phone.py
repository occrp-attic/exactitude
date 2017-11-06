import six
from banal import ensure_list
from phonenumbers import parse as parse_number
from phonenumbers import is_possible_number, is_valid_number, format_number
from phonenumbers import PhoneNumberFormat
from phonenumbers.phonenumberutil import NumberParseException

from exactitude.common import ExactitudeType


class PhoneType(ExactitudeType):

    def _clean_countries(self, countries):
        result = set([None])
        for country in ensure_list(countries):
            if isinstance(country, six.string_types):
                country = country.strip().upper()
                result.add(country)
        return result

    def clean_text(self, number, countries=None, **kwargs):
        """Parse a phone number and return in international format.

        If no valid phone number can be detected, None is returned. If
        a country code is supplied, this will be used to infer the
        prefix.

        https://github.com/daviddrysdale/python-phonenumbers
        """
        for country in self._clean_countries(countries):
            try:
                num = parse_number(number, country)
                if is_possible_number(num):
                    if is_valid_number(num):
                        return format_number(num, PhoneNumberFormat.E164)
            except NumberParseException:
                pass
