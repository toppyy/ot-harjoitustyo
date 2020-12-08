from tkinter import messagebox

def convert_to(data, coltype):


    if coltype == 'int':
        return [int(obs) for obs in data]

    if coltype == 'float':
        return [float(obs) for obs in data]


    return data
