# Random-Comments
This Utilitiy will choose a random comment from a file and copy on clipboard in one second interval. So that while commenting on social media platform you have to just paste on comment section. Every time you will get new random comment.

# Use Cases
- If you want to comment on social media and everytime you want to change you comment from predefined comment list to avoid your comments marked as a spam.
- Feel your users/followers that you are not posting same comments all the time.

# Installation
Install the dependencies and start the copy server.

```sh
cd <Current Directory>
python server.py
```
# How to Change Copier Timing interval
Navigate and open Server.py file on text editor.
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
# How To Add Comments
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

Apache License 2.0

# Contact Us
- Follow me on : [Facebook] | [Linkedin]
- Write me on : Lokesh16191@gmail.com

[Gmail]: <lokesh16191@gmail.com>
[Facebook]: <https://www.facebook.com/lokesh16191/>
[Linkedin]: <https://www.linkedin.com/in/lokesh16191/>

