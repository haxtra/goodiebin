#!/usr/bin/env python3

# App     : mdtoc - generate TOC from markdown file
# Repo    : https://github.com/haxtra/goodiebin
# License : MIT

from sys import argv, exit
import re

if len(argv) != 2:
	print('mdtoc - generate TOC from markdown file')
	print('')
	print(' usage:')
	print('  mdtoc <mdfile.md>')
	exit(1)

# load file
filepath = argv[1]
with open(filepath, 'r') as file:
    lines = file.read().split('\n')

# extract headers
headers = []
for line in lines:
	if line.startswith('#') and not line.startswith('# '):
		headers.append(line)

# build links
def kebabize(text):
	return text.strip().lower() \
	            .replace(' ', '-') \
	            .replace('&', '')

pattern = re.compile(r'^(#+)\s(.+)$', flags=0)

toc = []
for header in headers:
	res = pattern.match(header)
	mdlink = "- [%s](#%s)" % (res[2], kebabize(res[2]))
	toc.append(('\t' * (len(res[1])-2)) + mdlink)

# serve hot
print('\n'.join(toc))
