from generationException import LengthException
from random              import choice
from random              import shuffle
from random              import sample

class Generator():
    def __init__(self,length,maj,num,char):
        self.__length  = length
        self.__maj     = maj
        self.__num     = num
        self.__char    = char
        self.__genList = self.__charList()
        self.__psswd   = ""
        self.__genPsswd()

    def __str__(self):
        objstr = \
        "self.__length  =   "+ str(self.__length)+"\r\n"+\
        "self.__maj     =   "+ str(self.__maj)+"\r\n"+\
        "self.__num     =   "+ str(self.__num )+"\r\n"+\
        "self.__char    =   "+ str(self.__char)+"\r\n"
        return objstr

    def __charList(self):
        lGen = [chr(97+x) for x in range(25)]
       
        if self.__char == True :
            lGen += [chr(33+x) for x in range(13)]
            lGen += [chr(58+x) for x in range(6)]
            lGen += [chr(91+x) for x in range(5)]
            lGen += [chr(123+x) for x in range(3)]

        if self.__maj == True :
            lGen += [chr(65+x) for x in range(25)]

        if self.__num == True :
            lGen += [chr(48+x) for x in range(9)]

        for x in xrange(75):
            shuffle(lGen)
        return lGen
        

    def __genPsswd(self):
        if int(self.__length)<5 or int(self.__length)>64:
            raise LengthException
            system.exit(0)

        for i in xrange(int(self.__length)):
            self.__psswd += choice(self.__genList)

    def getPsswd(self):
        return self.__psswd