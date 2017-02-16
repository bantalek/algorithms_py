def toCamel(str): 
    iterable = str.split(" ")

    return iterable[0] + "".join([word[0].upper() + word[1:] for word in iterable[1:]])

print(toCamel("i want to be camel case"))