
import glob
import re
import os

for filepath in glob.glob("_posts/*md"):
    print(filepath)
    # Read in the file
    with open(filepath, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub(r'/photos/(.*)\.[a-zA-Z]*', r'\1.jpg', filedata)

    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)
