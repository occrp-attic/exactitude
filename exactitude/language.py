from normality import stringify

from exactitude.common import ExactitudeType


class LanguageType(ExactitudeType):

    def __init__(self, *args):
        super(LanguageType, self).__init__(*args)
        self.names = {}
        for code, label in self.locale.languages.items():
            self.names[code.lower()] = label

    def validate(self, text, **kwargs):
        text = stringify(text)
        if text is None:
            return False
        return text.lower() in self.names
