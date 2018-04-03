from __future__ import unicode_literals

import re
from stdnum import iban as iban_validator
from normality import stringify
from normality.cleaning import strip_quotes

from exactitude.common import ExactitudeType
from exactitude.domain import DomainType


class IbanType(ExactitudeType):
    domains = DomainType()

    def validate(self, iban, **kwargs):
#        iban = stringify(iban).replace(" ","")
        if iban is None:
            return False

        try:
            if iban_validator.is_valid(iban):
                return True
            elif not iban_validator.is_valid(iban):
                return False
        except iban.error:  # not a valid iban
            return False
        return True


    def clean(self, text, **kwargs):
        """Create a more clean, but still user-facing version of an
        instance of the type."""
        if text is not None:
            text = stringify(text).replace(" ","")
            return text
