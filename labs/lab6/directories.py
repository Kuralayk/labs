import os
import shutil

#1
def list_files(path):
    if not os.path.exists(path):
       print("Doesnt exist")
       return 
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print(os.listdir(path))

#2
def check(path):
    print(os.path.exists(path))
    print(os.access(path, os.R_OK))
    print(os.access(path, os.W_OK))
    print(os.access(path, os.X_OK))

#3
def check_path_details(path):
    if os.path.exists(path):
        print("Filename: ", os.path.basename(path))
        print("Directory: ", os.path.dirname(path))
    else:
        print("Path does not exist!")

#4
def write_list_to_file(filename, my_list):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in my_list:
            file.write(str(item) + '\n')
    print(f"List written to {filename}")

#5
def generate_text_files():
    for char in range(65, 91):
        with open(f"{chr(char)}.txt", 'w', encoding='utf-8') as file:
            file.write(f"This is file {chr(char)}.txt\n")
    print("26 files generated.")

#6
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File copied from {source} to {destination}")
    except FileNotFoundError:
        print("Source file not found!")

#7 
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File {path} deleted.")
        else:
            print("No write access to delete the file.")
    else:
        print("File does not exist!")