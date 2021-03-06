import re


def guesstype(datapart):
    """Guesses datatype from data

    Args:
        datapart: A list of data

    Returns:
        A string describing the data type
    """

    obs = datapart[0]  # Guess from one obs

    if re.search('[^0-9.,]', obs) is not None:
        return 'str'

    if re.search('[^0-9]', obs) is not None:
        return 'float'

    if re.search('[0-9]+', obs) is not None:
        return 'int'

    return 'str'
