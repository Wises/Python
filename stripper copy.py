#!/usr/bin/env python
from os import rename, listdir

badprefix = "4clubbers.pl"
badprefix2 = "[www.4Clubbers.pl]"
badprefix3 = "www.music4you.hu"
badprefix4 = "[www.]"
badprefix5 = "[4clubbers.com.pl]"
#path = "/Users/Wiseman/Desktop/M8x/"
#fnames = listdir('Users/Wiseman/Desktop/M8x/')
#fnamess = fnames
fnames = listdir('.')

print badprefix

for fname in fnames:
     rename(fname, fname.replace(badprefix, '', 5))

for fname in fnames:
    rename(fname, fname.replace(badprefix2, '', 5))

for fname in fnames:
    rename(fname, fname.replace(badprefix3, '', 5))

for fname in fnames:
    rename(fname, fname.replace(badprefix4, '', 5))

for fname in fnames:
    rename(fname, fname.replace(badprefix5, '', 5))
     
     




