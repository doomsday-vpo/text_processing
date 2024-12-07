# Write a program that reads a string from the console and
# replaces any sequence of the same letters with a single corresponding letter.

def replace_repeated_chars(text):
    if not text:
        return ""

    result = text[0]
    for i in range(1, len(text)):
        if text[i] != text[i - 1]:
            result += text[i]
    return result


text = input()

result = replace_repeated_chars(text)
print(result)
