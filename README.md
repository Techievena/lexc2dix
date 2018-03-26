# lexc2dix
A software that parses over the existing lttoolbox format and generates the corresponding monolingual dictionary in lttoolbox format. The package is modular and is user-friendly with proper help message and usage instructions. This was done as a part of coding challenge for the project `Extend lttoolbox to have the power of HFST`.

GETTING STARTED
---------------
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### CLONE THE REPOSITORY

```
$ git clone https://github.com/Techievena/lexc2dix.git
$ cd lexc2dix
```

### INSTALL PREREQUISITES

```
$ pip3 install -r requirements.txt
$ pip3 install -r test-requirements.txt
```

### INSTALL THE PACKAGE

```
$ python3 setup.py install
```

### USAGE

```
$ lexc2dix --help
usage: lexc2dix [-h] [-e] [-v] [filename]

lexc2dix

positional arguments:
  filename

optional arguments:
  -h, --help     show this help message and exit
  -e
  -v, --version

$ lexc2dix tests/test_files/apertium-kaz.kaz.lexc
```

As the package is currently buggy and can't handle all the entries present in the lexc files we are not writing the results into a dix file, but that be easily done manually with the help of this command:

```
$ lexc2dix tests/test_files/apertium-kaz.kaz.lexc | tee tests/test_files/apertium-kaz.kaz.dix
```

EXTERNAL LIBRARIES USED
-----------------------
* regex 2018.02.21 (Python 3)

CAPABILITIES AND POSSIBILITIES
------------------------------
The lexc2dix module is expected to function as follows:  

- [x] Parses over the lexc files.
- [x] Stores them in form of python dictionaries.
- [x] Generates the monolingual dictionary files.

CONTRIBUTION
------------
The work flow is the same as that of any other repository.

1.Fork / clone the repository.  
2.Create a new branch , say `my-changes` and make your changes in this branch.  
3.Commit your changes and send a Pull request (PR) to this repository.  

Active contributors would be rewarded with the tag of "Collabrators".  
Bug fixes , Issues , Issue solutions , Optimizations & Enhancements are always welcome.

LICENSE
-------
The GNU GENERAL PUBLIC LICENSE - [Abinash Senapati](http://github.com/Techievena) - All Rights Reserved.

ACKNOWLEDGEMENTS
----------------
I would like to thank mentors at [Apertium](https://github.com/Apertium) for helping me in the development and maintenance of this package.