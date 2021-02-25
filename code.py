
# read the file of type file into content
with open("a_example", 'r') as fp:
    content = fp.read()

print(type(content))
print(content)

with open("result.txt", "w") as text_file:
    text_file.write(content)

