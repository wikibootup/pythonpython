#!/usr/bin/env python

fr = open('python_Dockerfile', 'r')
fw = open('Dockerfile', 'w')
a = fr.read()
try:
    a = a.replace('<x.y.z>', '2.6.7')
    a = a.replace('<x.y>', '2.6')
except:
    print "error in replacing string"
else:
    print a
