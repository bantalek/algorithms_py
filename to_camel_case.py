def to_camel(str): 
    words = str.split(" ")
    first_word = words[0]
    return  first_word + "".join([word[0].upper() + word[1:] for word in words[1:]])

print(toCamel("i want to be camel case"))