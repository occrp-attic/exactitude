from urlnormalizer import normalize_url, is_valid_url

from exactitude.common import ExactitudeType


class UrlType(ExactitudeType):

    def validate(self, url, **kwargs):
        """Check if `url` is a valid URL."""
        return is_valid_url(url)

    def clean_text(self, url, **kwargs):
        """Perform intensive care on URLs, see `urlnormalizer`."""
        return normalize_url(url)
