# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

def find_emoticons(text):
    emoticons = []
    for i in range(len(text) - 1):
        if text[i] == ':' and text[i + 1] != ' ':
            emoticons.append(text[i] + text[i + 1])
    return emoticons

text = input()

emoticons = find_emoticons(text)
for emoticon in emoticons:
    print(emoticon)
