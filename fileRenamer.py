"""
Author: Clint Kline
Date Created: 5/26/2021 
Last Modified: 06/01/2021
Purpose: Renames JPG, PNG, and GIF image files by type in a folder in numeric order beginning with 01.

-------------------------------------------------

Instructions: 
- Paste file in desired folder. 
- Open file in your favorite code editor.
- Execute file.

-- OR --

- Open CMD prompt
- type "python <path>/fileRenamer.py"

--------------------------------------------------

- If youd like to rename a file with a different extension:
    1. replace one of the current extensions with the desired one @ either locations 1 & 4, 2 & 5, or 3 & 6. 
    2. create an additional function for the desired extension by copy/pasting one of the existing 
    functions, and replace the extention in the new function. 

"""


import os

folder = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(folder)
# print filepath
print("\n" + folder + "\n")
# print list of current file names
print(files)
# starting number
count = 1
# begin renaming
for file in files:
    jpg = ['.JPG', '.jpg', '.jpeg']  # file extension location 1
    png = ['.PNG', '.png']  # file extention location 2
    gif = ['.GIF', '.gif']  # file extension location 3

    # JPG Copy
    if file.endswith(tuple(jpg)):
        try:
            os.rename(folder + '\\' + file, folder + '\\' + '0' +
                      str(count) + '.jpg')  # file extension location 4
            count = count + 1
        except OSError as e:
            print("\nError No: ", e.errno)
            print(str(file) + " already exists.")

    # PNG Copy
    if file.endswith(tuple(png)):
        try:
            os.rename(folder + '\\' + file, folder + '\\' + '0' +
                      str(count) + '.png')  # file extension location 5
            count = count + 1
        except OSError as e:
            print("\nError No. : ", e.errno)
            print(str(file) + " already exists.")

    # GIF Copy
    if file.endswith(tuple(gif)):
        try:
            os.rename(folder + '\\' + file, folder + '\\' + '0' +
                      str(count) + '.gif')  # file extension location 6
            count = count + 1
        except OSError as e:
            print("\nError No. : ", e.errno)
            print(str(file) + " already exists.")

# renaming completed confirmation
print("\nAll files successfully renamed as:\n")

# display sorted list of new names
files = os.listdir(folder)
print(sorted(files, key=len))
