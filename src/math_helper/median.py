

def median(data):
    data = sorted(data)

    midpoint = len(data) // 2

    if len(data) % 2 == 1:
        return data[midpoint]

    return sum(data[(midpoint-1):(midpoint+1)]) / 2
