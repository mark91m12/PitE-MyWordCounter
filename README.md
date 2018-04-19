# MyWordCounter

[![Build Status](https://travis-ci.org/mark91m12/PitE-MyWordCounter.svg?branch=master)](https://travis-ci.org/mark91m12/PitE-MyWordCounter) [![Coverage Status](https://coveralls.io/repos/github/mark91m12/PitE-MyWordCounter/badge.svg)](https://coveralls.io/github/mark91m12/PitE-MyWordCounter) [![HitCount](http://hits.dwyl.io/mark91m12/PitE-MyWordCounter.svg)](http://hits.dwyl.io/mark91m12/PitE-MyWordCounter)


**MyWordCounter** is an implementation of the Linux program WC ([Word Counter](https://en.wikipedia.org/wiki/Wc_(Unix))) 

This is the first task of the course "Python in the Enterprise", as requested have been implemented the following functions :

* count_lines
* count_words
* count_characters

### Requirements
In order to run the program you only need to install [python](https://www.python.org/downloads/) 3.6.

### Usage

the execution of the program is quite simple, just run the following command inside the folder where the file MyWordCounter.py is located followed by one of the functions (optional) and obviously the file's path (or simply the filename if this one is located in the same folder of the program).
  
```shell
$ python3 myWC.py [option] <filename>
```

### Possible options :

output : number of lines inside the file

```shell
$ python3 myWC.py -l <filename>
```
output : number of words inside the file

```shell
$ python3 myWC.py -w <filename>
```
output : number of characters inside the file

```shell
$ python3 myWC.py -c <filename>
```

**_IF NO OPTION IS INDICATED ALL COUNTS WILL BE PRINTED IN THIS ORDER_**

lines number - words number - characters number

**_IN CASE OF NO FILE THE PROGRAM READ STANDARD INPUT_**

to terminate the std input press <kbd>CTRL</kbd>+<kbd>D</kbd>

### Example

In this example we can see the results when no file is indicated as input and it's choosed the option -w (number of words)
```shell
$ python3 myWC.py -w
hello this is an example
press ctrl+D to close the standard input
12
$ _
```
### Author

* **Marco Amato**  - [other projects](https://github.com/mark91m12)
