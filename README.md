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


# MIT License

Copyright (c) 2017: Journalism Development Network, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
