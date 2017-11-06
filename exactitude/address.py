import re
from normality import normalize as normalize_text
from normality.cleaning import collapse_spaces

from exactitude.common import ExactitudeType


class AddressType(ExactitudeType):
    LINE_BREAKS = re.compile(r'(\r\n|\n|<BR/>|<BR>|\t|ESQ\.,|ESQ,|;)')
    COMMATA = re.compile(r'(,\s?[,\.])')

    def clean_text(self, address, **kwargs):
        """Basic clean-up."""
        address = self.LINE_BREAKS.sub(', ', address)
        address = self.COMMATA.sub(', ', address)
        address = collapse_spaces(address)
        if len(address):
            return address

    def normalize(self, address, **kwargs):
        """Make the address more compareable."""
        # TODO: normalize well-known parts like "Street", "Road", etc.
        # TODO: consider using https://github.com/openvenues/pypostal
        addresses = super(AddressType, self).normalize(address, **kwargs)
        return [normalize_text(a) for a in addresses]
