def error_code_message(err=0, filename=''):
    """string"""
    if err == 0:
        return "Success!"
    elif err == 2:
        return "File " + filename + " not found."
    elif err == 32:
        return "File " + filename + " opened in another program."
    else:
        return "Error" + str(err) + "."
