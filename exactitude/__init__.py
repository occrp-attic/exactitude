from exactitude.url import UrlType
from exactitude.name import NameType
from exactitude.domain import DomainType
from exactitude.email import EmailType
from exactitude.ipv4 import Ipv4Type
from exactitude.ipv6 import Ipv6Type
from exactitude.iban import IbanType
from exactitude.address import AddressType
from exactitude.date import DateType
from exactitude.phone import PhoneType
from exactitude.country import CountryType
from exactitude.language import LanguageType
from exactitude.identifier import IdentifierType
from exactitude.common import TextType

urls = UrlType()
names = NameType()
domains = DomainType()
emails = EmailType()
ipv4s = Ipv4Type()
ipv6s = Ipv6Type()
ibans = IbanType()
addresses = AddressType()
dates = DateType()
phones = PhoneType()
countries = CountryType()
languages = LanguageType()
identifiers = IdentifierType()
texts = TextType()

__all__ = [urls,
           names,
           domains,
           emails,
           ipv4s,
           ipv6s,
           ibans,
           addresses,
           dates,
           phones,
           countries,
           languages,
           identifiers,
           texts]
