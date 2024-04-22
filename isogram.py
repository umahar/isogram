def is_isogram(string):
    char_count=0
    for char in string.lower():
        if not char.isalpha():
            continue
        char_count = string.lower().count(char)
        if char_count>1:
            break
    return not char_count>1
        

print(is_isogram("Alphabet"))
