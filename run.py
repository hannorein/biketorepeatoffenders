#!/bin/python
import os
import sys
import glob
os.system("twphotos -u "+sys.argv[1])
for f in glob.glob(sys.argv[1]+"/*.*"):
    os.system("alpr "+f+ " |grep confidence | sed -e 's/^/"+f.replace("/","\/")+"/' >> out_"+sys.argv[1]+".txt")
