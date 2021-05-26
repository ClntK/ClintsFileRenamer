"""
Author: Clint Kline
Date Created: 5/26/2021 1:08 AM
Purpose: Renames all .JPG files in a folder in numeric order beginning with 01.
Instructions: 
- Paste file in desired folder. 
- Open file in your favorite code editor.
- Execute file.

-- OR --

- Open CMD prompt
- type "python <path>/fileRenamer.py"

- if youd like to rename a file with a different extension, simply replace the current extensions with the desired ones @ locations 1 & 2. 
"""


import os

folder = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(folder)
#print filepath
print("\n" + folder + "\n")
#print list of current file names
print(files)
#starting number
count = 1
#begin renaming
for file in files:
    ext = ['.JPG', '.jpg'] # file extension location 1
    if file.endswith(tuple(ext)): 
        os.rename(folder + '\\' + file, folder + '\\' + '0' + str(count) + '.jpg') # file extension location 2
        count = count + 1
#renaming complete
print("\nAll files successfully renamed as:\n")

files = os.listdir(folder)
# print renamed files sorted in ascending order
print(sorted(files, key=len))
