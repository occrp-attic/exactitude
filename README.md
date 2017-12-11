# exactitude

[![Build Status](https://travis-ci.org/alephdata/exactitude.svg?branch=master)](https://travis-ci.org/alephdata/exactitude)

``exactitude`` contains parsers and validators for common text data types, such as
phone numbers, dates, URLs, domain names, email addresses and country names. It
can be used to normalize source data before further processing.

Most of the functionality of ``exactitude`` is provided by third-party packages
which are imported and exposed in a uniform way.


## Dates

Dates in ``exactitude`` are handled as ISO 8601 prefixes. That means that valid
dates can indicate a loss of precision by shortening dates down to either a
year (``2017``), or a year-month combination (``2017-02``).

If a date is not recognized as a valid ISO 8601 prefix and no format has been
specified, ``exactitude`` will attempt to recognize the format used.


## Name

> ... In that Empire, the Art of Cartography attained such Perfection that the map of
> a single Province occupied the entirety of a City, and the map of the Empire, the
> entirety of a Province. In time, those Unconscionable Maps no longer satisfied, and
> the Cartographers Guilds struck a Map of the Empire whose size was that of the Empire,
> and which coincided point for point with it. The following Generations, who were not
> so fond of the Study of Cartography as their Forebears had been, saw that that vast
> map was Useless, and not without some Pitilessness was it, that they delivered it up
> to the Inclemencies of Sun and Winters. In the Deserts of the West, still today,
> there are Tattered Ruins of that Map, inhabited by Animals and Beggars; in all the
> Land there is no other Relic of the Disciplines of Geography.

purportedly from Suárez Miranda, Travels of Prudent Men, Book Four, Ch. XLV, Lérida, 1658