import re

def guesstype(datapart):

    obs = datapart[0]  # Guess from one obs

    if re.match('[^0-9.,]', obs) is not None:
        return 'str'

    if re.match('[^0-9]', obs) is not None:
        return 'float'

    if re.match('[0-9]+', obs) is not None:
        return 'int'

    return 'str'