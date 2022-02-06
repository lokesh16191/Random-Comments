import pyperclip
import time
import random

with open('comments.txt', 'r', encoding="utf8") as infile:
    data = infile.read()  # Read the contents of the file into memory.
# Return a list of the lines, breaking at line boundaries.
li = data.splitlines()

while True:
    time.sleep(1) #Time interval for copy
    pyperclip.copy(random.choice(li))
    print(random.choice(li))