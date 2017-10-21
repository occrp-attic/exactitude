import countrynames

from dalet.locale import locale

COUNTRY_NAMES = {
    'zz': 'Global',
    'eu': 'European Union',
    'xk': 'Kosovo',
    'yucs': 'Yugoslavia',
    'csxx': 'Serbia and Montenegro',
    'suhh': 'Soviet Union',
    'ge-ab': 'Abkhazia',
    'x-so': 'South Ossetia',
    'so-som': 'Somaliland',
    'gb-wls': 'Wales',
    'gb-sct': 'Scotland',
    'md-pmr': 'Transnistria'
}

for code, label in locale.territories.items():
    COUNTRY_NAMES[code.lower()] = label


def is_country_code(code):
    if code is None:
        return False
    return code.lower() in COUNTRY_NAMES.keys()


def parse_country(country, guess=True):
    """Determine a two-letter country code based on an input.

    The input may be a country code, a country name, etc.
    """
    if guess:
        country = countrynames.to_code(country)
    if country is not None:
        country = country.lower()
        if is_country_code(country):
            return country
