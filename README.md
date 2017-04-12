# PasswordGenerator
**Little password generator python script**

## Usage
### Basic usage
python main.py
This will run the script with the basic options: 
  * 16 chars
  * Without numbers
  * Without upper case
  * Without symbols/special chars
 
## Available options
This script comes with some features:
* -l [length]        Enter the password length (must be more than 4 and less than 64
* -c                 To enable special chars
* -m                 To enable upper case
* -n                 To enable numbers

## Exemples
* ~$ python main.py  
 ygomxitobkuyekhn

* ~$ python main.py -l 32  
 asibigklmqpibptblmhrbogsahqivxpt

* ~$ python main.py -c  
 i>_?euhv=[$n#;r=

* ~$ python main.py -m   
 QGAyhLtIksUErVvQ

* ~$ python main.py -n  
 sktc4mwk1wlu1tf0

## Planned features
* Add a non-repeat option for password
* Add an option to store the generated password inside a file
