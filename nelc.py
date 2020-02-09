#!/usr/bin/env python
import sys,re

if len(sys.argv) < 2:
    exit(1)

src = sys.argv[1]
dest = re.sub(r'\/\?userid=(\d+)', r'', src.replace('/song/','/#/song?id='))
print(dest)
exit(0)
