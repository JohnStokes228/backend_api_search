import string


def clean_str(input_str: str) -> str:
    """Clean str in standard way.
    Parameters
    ----------
    input_str : String, but if it's not up to snuff we'll be changing it!

    Notes
    -----
    Slight risk of being overly sweaty here, but the 'translate' method is orders of magnitude faster to run than
    alternatives according to benchmarks. Hopefully I don't forget what its doing!!!

    Returns
    -------
    str
        The desired string but clean.
    """
    trans_table = str.maketrans(' ', '_', string.punctuation)
    res = input_str.translate(trans_table)

    return res
