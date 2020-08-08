def validate_input(data_type=str, *args):
    for arg in args:
        if not isinstance(arg, data_type):
            return False
    return True
