# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

def length_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def characters_are_valid(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True

def no_redundant_symbols(username):
    if " " in username:
        return False
    return True


def username_is_valid(username):
    if length_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True
    return False



usernames = input().split(", ")

for username in usernames:
    if username_is_valid(username):
        print(username)