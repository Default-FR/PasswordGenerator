import random
from random  import choice
from random  import shuffle
from random  import sample

import generationException
from generationException import LengthException

SHUFFLE_LIM = 75

MIN_SIZE = 8
MAX_SIZE = 64

class Generator():
    """References the generator

    Attributes:
        __length  : password size
        __maj     : contains majs
        __num     : contains numbers
        __char    : contains special chars
        __genList : char list for the generation
        __psswd   : generated password
    """
    def __init__(self, length, maj, num, char):
        self.__length  = int(length)
        self.__maj     = maj
        self.__num     = num
        self.__char    = char
        self.__genList = self.__charList()
        self.__psswd   = ""
        self.__genPsswd()

    def __str__(self):
        """Prints password and its generation details
        """
        psswdstr = "size  : {}\n"
        psswdstr+= "maj   : {}\n"
        psswdstr+= "num   : {}\n"
        psswdstr+= "char  : {}\n"
        psswdstr+= "\n"
        psswdstr+= "final : {}\n"
        return psswdstr.format(
                self.__length,
                self.__maj,
                self.__num,
                self.__char,
                self.__psswd
            )

    def __charList(self):
        """Generate password generator's alphabet

        First add each alphabet
        Then shuffle the list

        Returns:
            lGen : list containing the alphabet
        """
        lGen = [chr(97+x) for x in range(25)]
       
        if self.__char :
            lGen += [chr(33+x) for x in range(13)]
            lGen += [chr(58+x) for x in range(6)]
            lGen += [chr(91+x) for x in range(5)]
            lGen += [chr(123+x) for x in range(3)]

        if self.__maj :
            lGen += [chr(65+x) for x in range(25)]

        if self.__num :
            lGen += [chr(48+x) for x in range(9)]

        for _ in range(SHUFFLE_LIM):
            shuffle(lGen)

        return lGen
        
    def __genPsswd(self):
        """Generate the password

        Check password size
        Then add randomly a char until the max size
        """
        if not MIN_SIZE <= self.__length <= MAX_SIZE:
            raise LengthException
            system.exit(0)

        for _ in range(self.__length):
            self.__psswd += choice(self.__genList)

    def get_password(self):
        """Returns the generated password
        """
        return self.__psswd
