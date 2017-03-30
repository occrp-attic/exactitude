import fingerprints
from normality import stringify


def make_fingerprint(text):
    """Generate a normalised company or person name, useful for comparison."""
    text = stringify(text)
    if text is None:
        return
    return fingerprints.generate(text)
