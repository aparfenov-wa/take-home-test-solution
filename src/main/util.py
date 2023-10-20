def filter_not_null_keys(pair):
    key, value = pair
    if value == None:
        return False
    else: 
        return True