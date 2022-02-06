# Random-Comments
This Utilitiy will choose a random comment from a file and copy on clipboard in one second interval. So that while commenting on social media platform you have to just paste on comment section. Every time you will get new random comment.
#Installation
Install the dependencies and start the copy server.

```sh
cd <Current Directory>
python server.py
```
#How to Change Copier Timings in Server.py

```sh
with open('comments.txt', 'r', encoding="utf8") as infile:
    data = infile.read()  # Read the contents of the file into memory.
# Return a list of the lines, breaking at line boundaries.
li = data.splitlines()

while True:
    time.sleep(1) #Time interval for copy in Seconds
    pyperclip.copy(random.choice(li))
    print(random.choice(li))
```
#How To Add Comments
Add your comments in comments.txt file. Each new line treat as a comment.

```sh
Hi
Hello
How Are You
Thanks
Thanks alot
Thank You So Much
```
# License

MIT

**Free Software, Hell Yeah!**
