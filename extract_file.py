# Write a program that reads the path to a file and subtracts the file name and its extension.

def extract_file_info(file_path):
    file_full = file_path.split('\\')[-1]
    file_name, file_extension = file_full.split('.')

    return file_name, file_extension


file_path = input()
name, extension = extract_file_info(file_path)

print(f"File name: {name}")
print(f"File extension: {extension}")
