import countrynames
from pycountry import countries

from dalet.validate import format_checker

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

for country in countries:
    code = country.alpha_2.lower()
    if hasattr(country, 'common_name'):
        COUNTRY_NAMES[code] = country.common_name
    else:
        COUNTRY_NAMES[code] = country.name


@format_checker.checks('country-code')
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
