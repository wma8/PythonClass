def capitalize(word):
    return word[0].upper() + word[1:].lower()

def titlify(s):
    result = []
    words = s.split()
    if words:
        result.append(capitalize(words[0]))
    for word in words[1:]:
        if len(word) > 3:
            result.append(capitalize(word))
        else:
            result.append(word.lower())
    return " ".join(result)
