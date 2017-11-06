from normality.cleaning import collapse_spaces

from exactitude.common import ExactitudeType


class NameType(ExactitudeType):

    def clean_text(self, name, **kwargs):
        """Basic clean-up."""
        return collapse_spaces(name)
