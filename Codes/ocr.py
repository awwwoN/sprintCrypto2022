#! /usr/bin/env python3
from png import Reader
from sys import argv, stdout, stderr, exit
from zlib import decompress

if len(argv) != 2:
    print(f"usage {argv[0]}' im.png", file=stderr)
    print(f"    extract iTxt chunks", file=stderr)
    exit(1)

def process(s):
    x=s.index(0)
    s=s[x+1:]
    assert s[0]==1 and s[1]==0
    s=s[2:]
    x=s.index(0)
    s=s[x+1:]
    x=s.index(0)
    s=s[x+1:]
    print(decompress(s).decode())

png=Reader(argv[1])
for (ty, oo) in png.chunks():
    if ty == b'iTXt':
        process(oo)
