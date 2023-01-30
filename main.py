"""python script used to compare 2 text files and save the difference in a new txt file."""

import os
import time

not_found_file1 = ["not found in file 2 but in file 1: ",]
not_found_file2 = [ "not found in file 1 but in file 2",]

file1_path = input("enter path to file 1: ")
file2_path = input("enter path to file 2: ")

with open(file1_path, 'r') as f1:
    file1 = f1.readlines()

with open(file2_path, 'r') as f2:
    file2 = f2.readlines()

with open('not_found_file.txt', 'w') as not_found_file:

    not_found_file.write("\nnot found in file 2 but in file 1: \n\n")

    for item in file1:
        if item in file2:
            print(f'item match: {item}')
        else:
            not_found_file1.append(item)
            not_found_file.write(item)

    not_found_file.write("\nnot found in file 1 but in file 2: \n\n")

    for item in file2:
        if item in file1:
            print(f'item match: {item}')
        else:
            not_found_file2.append(item)
            with open(file2_path, 'r') as f2:
                file2 = f2.readlines()
                not_found_file.write(item)

not_found_file.close()
if not_found_file1 or not_found_file2:
    print(not_found_file1 + not_found_file2)
    path = str(os.getcwd()) + "\\not_found_file.txt"
    newPath = path.replace(os.sep, '/')
    os.system("start " + newPath)
    time.sleep(.02)
    print(path)
else:
    print('both files match')
