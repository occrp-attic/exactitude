from __future__ import unicode_literals

from normality import stringify
from stdnum import iban as iban_validator

from exactitude.common import ExactitudeType
from exactitude.domain import DomainType


class IbanType(ExactitudeType):
    domains = DomainType()

    def validate(self, iban, **kwargs):
        iban = stringify(iban)
        if iban is None:
            return False

        try:
            return iban_validator.is_valid(iban)
        except iban.error:  # not a valid iban
            return False

    def clean_text(self, text, **kwargs):
        """Create a more clean, but still user-facing version of an
        instance of the type."""
        if text is not None:
            text = stringify(text).replace(" ", "")
            return text
