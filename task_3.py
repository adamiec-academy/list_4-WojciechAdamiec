def min_max(data):
    min_val = data[0]
    max_val = data[0]
    for value in data:
        if value > max_val:
            max_val = value
        elif value < min_val:
            min_val = value
    return min_val, max_val
