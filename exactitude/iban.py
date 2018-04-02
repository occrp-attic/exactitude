from __future__ import unicode_literals

import re
from stdnum import iban as iban_validator
from normality import stringify
from normality.cleaning import strip_quotes

from exactitude.common import ExactitudeType
from exactitude.domain import DomainType


class IbanType(ExactitudeType):
    IBAN_REGEX = re.compile('([a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16})')
    domains = DomainType()


    def validate(self, iban, **kwargs):
        iban = stringify(iban)
        if iban is None:
            return
        if not self.IBAN_REGEX.match(iban):
            return False

        try:
            if iban_validator.is_valid(iban):
                return True
        except iban.error:  # not a valid iban
            return False
        return True


    def clean(self, text, **kwargs):
        """Create a more clean, but still user-facing version of an
        instance of the type."""
        text = stringify(text)
        if text is not None:
            return self.clean_text(text, **kwargs)

    def clean_text(self, text, **kwargs):
        return text
