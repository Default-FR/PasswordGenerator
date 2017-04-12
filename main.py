#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from getopt    import getopt
from getopt    import GetoptError
from sys       import argv
from sys       import exit

def usage():
    print "usage:"
    print "   -l [length]        Enter the password length (4<l<32)"
    print "   -c                 To enable special chars"
    print "   -m                 To enable upper case"
    print "   -n                 To enable numbers"

if __name__ == '__main__':

    char   = False
    length = 16
    maj    = False
    num    = False

    try:
        opts, args = getopt(argv[1:], "chnml:", ["help", "output="])

    except GetoptError as err:
        print str(err)
        usage()
        exit(2)

    for o, a in opts:
        if o == "-c":
            char = True
        elif o in ("-h", "--help"):
            usage()
            exit()
        elif o in ("-l"):
            length = a
        if o == "-m":
            maj = True
        if o == "-n":
            num = True

    g = Generator(length,maj,num,char)
    print(g.getPsswd())
