# PasswordGenerator
**Little password generator python script**

## Usage
### Basic usage
python main.py or ./main.py -- depending of how you named the script

This will run the script with the basic options: 
  * 32 chars
  * Without numbers
  * Without upper case
  * Without symbols/special chars
 
### Available options
This script comes with some features:
* -l [length]        Enter the password length (must be more than 4 and less than 64
* -c                 To enable special chars
* -m                 To enable upper case
* -n                 To enable numbers

## Examples 
Basic feature
```shell
~$ python3 main.py  
size  : 32
maj   : False
num   : False
char  : False

final : oeoqbbbruawtuoqgpxqkweiefrwwbmuc
```

Custom length
```shell
~$ python3 main.py -l 16
size  : 16
maj   : False
num   : False
char  : False

final : yaqvwkcmdrcomcii
```

Add chars
```shell
~$ python3 main.py -c
size  : 32
maj   : False
num   : False
char  : True

final : ;!h>_&qi<,&b&d:x=kbb(u<|^,-deh()
```

Add majs
```shell
~$ python3 main.py -m
size  : 32
maj   : True
num   : False
char  : False

final : NqaxXgmTrEYQXoTporeUsdnHJYGgMvMP
```

Add numbers
```shell
~$ python3 main.py -n
size  : 32
maj   : False
num   : True
char  : False

final : pc0ehify4ok2k27i1dfec2q7gkwnglsv
```

## Planned features
- [x] make documentation
- [x] switched to python3
- [x] copy to clipboard
