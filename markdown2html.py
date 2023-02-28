#!/usr/bin/python3

import markdown
import os.path
import sys


if len(sys.argv) < 2:
    print('Usage: ./markdown2html.py README.md README.html')
    exit (1)
elif os.path.isfile('./README.md'):
    with open(sys.argv[0], 'r') as f:
        text = f.read()
    html = markdown.markdown(text)
    print(html)

    with open(sys.argv[1], 'w') as f:
        f.write(html)
    exit (1)
else:
    print('Missing README.md')
    exit (0)
