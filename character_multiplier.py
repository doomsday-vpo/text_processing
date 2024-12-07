# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and
#     add the result to the total sum, then continue with the next two characters.
#     If one of the strings is longer than the other,
# add the remaining character codes to the total sum without multiplication.

def char_multiplier(str1, str2):
    total_sum = 0
    min_length = min(len(str1), len(str2))

    for i in range(min_length):
        total_sum += ord(str1[i]) * ord(str2[i])

    if len(str1) > len(str2):
        for i in range(min_length, len(str1)):
            total_sum += ord(str1[i])
    elif len(str2) > len(str1):
        for i in range(min_length, len(str2)):
            total_sum += ord(str2[i])

    return total_sum


str1, str2 = input().split()
result = char_multiplier(str1, str2)
print(result)
