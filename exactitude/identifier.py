from normality import normalize

from exactitude.common import ExactitudeType


class IdentifierType(ExactitudeType):
    """Used for registration numbers, codes etc."""

    def normalize(self, text, **kwargs):
        """Normalize for comparison."""
        identifiers = []
        for ident in super(IdentifierType, self).normalize(text, **kwargs):
            identifiers.append(normalize(ident))
        return identifiers
