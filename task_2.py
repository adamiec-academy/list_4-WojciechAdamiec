def my_split(text):
    result = []
    current_word = ""

    for letter in text:
        if letter != " ":
            current_word += letter
        elif current_word != "":
            result.append(current_word)
            current_word = ""
    
    if current_word != "":
        result.append(current_word)
    
    return result
