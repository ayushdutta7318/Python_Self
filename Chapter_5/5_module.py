# Modules in python: modules are pre written code by someone else so you dont have to write basic code again.

# there are 2 types of moidule: built in and expternal

# built in example: check the list of other in built module

import math;

print(math.sqrt(16));

# external module: it can be written by us or we can use pip: python's package manager:

import mymodule;

mymodule.hello();

# lets install external module using pip: in terminal write: pip install requests
import requests;

r = requests.get("https://www.google.com");
print(r.text);

import pyjokes;
joke = pyjokes.get_joke();
print(joke);