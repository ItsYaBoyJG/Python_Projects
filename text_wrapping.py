import textwrap

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
max_width = 4

l = " ".join(textwrap.wrap(string, max_width))
print(textwrap.fill(l))
