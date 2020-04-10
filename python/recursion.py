def get_length(x):
    if len(x) <= 1:
        return 1
    return get_length(x[:-1]) + 1

print(get_length("123sd"))