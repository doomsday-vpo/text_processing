# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII
# table. For example, A would be replaced with D, B would become E, and so on.
# Print the encrypted text.

normal_string = input()
encrypted_string = ""
for char in normal_string:
    encrypted_char = chr(ord(char) + 3)
    encrypted_string += encrypted_char

print(encrypted_string)