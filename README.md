# dalet

``dalet`` contains parsers and validators for common text data types, such as
phone numbers, dates, URLs, domain names, email addresses and country names. It
can be used to normalize source data before further processing.

Most of the functionality of ``dalet`` is provided by third-party packages
which are imported and exposed in a uniform way.


### Dates

Dates in ``dalet`` are handled as ISO 8661 prefixes. That means that valid
dates can indicate a loss of precision by shortening dates down to either a
year (``2017``), or a year-month combination (``2017-02``).

If a date is not recognized as a valid ISO 8661 prefix and no format has been
specified, ``dalet`` will attempt to recognize the format used.
