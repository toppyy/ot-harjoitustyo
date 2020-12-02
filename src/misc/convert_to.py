from tkinter import messagebox

def convert_to(data, coltype, column_name):

    try:
        if coltype == 'int':
            data = [int(obs) for obs in data]

        if coltype == 'float':
            data = [float(obs) for obs in data]

    except ValueError:
        error_msg = 'Error converting column {} to {}'.format(column_name,coltype)
        error_msg = error_msg + '\nReturning column as str.'
        messagebox.showwarning(message=error_msg)
        coltype='str'

    return {
        "data": data,
        "coltype": coltype
    }
