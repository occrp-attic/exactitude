from exactitude.url import UrlType
from exactitude.domain import DomainType
from exactitude.email import EmailType
from exactitude.address import AddressType
from exactitude.date import DateType
from exactitude.phone import PhoneType
from exactitude.country import CountryType
from exactitude.language import LanguageType

urls = UrlType()
domains = DomainType()
emails = EmailType()
addresses = AddressType()
dates = DateType()
phones = PhoneType()
countries = CountryType()
languages = LanguageType()

__all__ = [urls,
           domains,
           emails,
           addresses,
           dates,
           phones,
           countries,
           languages]
