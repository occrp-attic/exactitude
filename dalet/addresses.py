import re
import countrynames
from normality import stringify
from normality.cleaning import remove_control_chars, collapse_spaces

LINE_BREAKS = re.compile(r'(\r\n|\n|<BR/>|\t|ESQ\.,|ESQ,|;)')
REMOVE = re.compile(r'(ATTENTION|ATTN|C/O|UNDELIVERABLE DOMESTIC ADDRESS)')
COMMATA = re.compile(r'(,\s?[,\.])')


def clean_address(address):
    address = stringify(address)
    if address is None:
        return
    address = address.upper()
    address = LINE_BREAKS.sub(', ', address)
    address = REMOVE.sub(' ', address)
    address = COMMATA.sub(', ', address)
    address = remove_control_chars(address)
    address = collapse_spaces(address)

    # return none if this is just a country code or name:
    code = countrynames.to_code(address, fuzzy=False, warn=False)
    if code is not None:
        return
    return address
