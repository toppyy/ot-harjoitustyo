
def convert_to(data, coltype):
    """Datatype conversion for lists

    Args:
        data: List of data to be converted
        coltype: Target datatype. Either int or float

    Returns:
        List. Converted data.
    """


    if coltype == 'int':
        return [int(float(obs)) for obs in data]

    if coltype == 'float':
        return [float(obs) for obs in data]

    return data
