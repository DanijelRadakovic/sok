def convert_to_float(number,default=0.0):
    try:
        value=float(number)
        return value,True
    except:
        value=default
        return value, False

def convert_to_boolean(number,default=False):
    try:
        value=bool(number)
        return value,True
    except:
        value=default
        return value, False