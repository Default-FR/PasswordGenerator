#!/usr/bin/env python
# -*- coding: utf-8 -*-

import generator
from generator import MAX_SIZE
from generator import MIN_SIZE
from generator import Generator

import getopt
from getopt    import getopt
from getopt    import GetoptError

import tkinter
from tkinter import Tk

import sys
from sys       import argv
from sys       import exit

import os
from os import system

DEFAULT_SIZE = 32
EXIT_FAILURE = 1
EXIT_SUCCESS = 0

def print_usage(err_ret):
    msg = 'usage:'
    msg+= '\t-l [length] Enter the password length ({} < l < {})'
    msg+= '\t-c          To enable special chars'
    msg+= '\t-m          To enable upper case'
    msg+= '\t-n          To enable numbers'
    print (msg.format(MIN_SIZE, MAX_SIZE))
    exit (err_ret)

def save_to_clipboard (psswd) :
    system('echo ' + psswd + '| clip')

if __name__ == '__main__':
    char   = False
    maj    = False
    num    = True
    length = DEFAULT_SIZE

    try:
        opts, args = getopt (
            argv[1:], 
            'chnml:', 
            ['help', 'output=']
        )
    except GetoptError as err:
        print(str(err))
        print_usage (EXIT_FAILURE)

    for o, a in opts:
        if o is '-c':
            char = True
        elif o in ('-h', '--help'):
            print_usage(EXIT_SUCCESS)
        elif o in ('-l'):
            length = a
        if o is '-m':
            maj = True
        if o is '-n':
            num = True

    g = Generator (length, maj, num, char)
    password = g.get_password()
    print(g)

    save_to_clipboard(g.get_password())
