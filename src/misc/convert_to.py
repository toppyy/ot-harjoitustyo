from tkinter import messagebox

def convert_to(data, coltype, column_name):

    try:
        if coltype == 'int':
            data = [int(obs) for obs in data]

        if coltype == 'float':
            data = [float(obs) for obs in data]

    except ValueError:
        messagebox.showwarning(message='Error converting column {} to {}. \nReturning column as str.'.format(column_name,coltype))
        coltype='str'

    return {
        "data": data,
        "coltype": coltype
    }
