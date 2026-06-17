"""import math

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,3))

from math import sqrt

print(sqrt(49))

import random
import string
random_letter=random.choice(string.ascii_letters)
print(random_letter)
print(random.randrange(2,10))
random_letter=random.choice(string.ascii_lowercase)
print(random_letter)
random_letter=random.choice(string.ascii_uppercase)
print(random_letter)
list1=[10,50,30,12,52]
print(random.choice(list1))

#Try out multiple random generation

#Try out secret module

import datetime

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.today()-datetime.timedelta(1))

#Try out random dates inbetween specific dates

import sys

print(sys.platform)
print(sys.version)

import os

print(os.getcwd())
print(os.listdir())

#Aliasing

import datetime as dt

print(dt.datetime.now())

import requests

url=requests.get('https://jsonplaceholder.typicode.com/users')
print(url.json())"""
import random
list1=[10,50,30,12,52]
for i in range(3):
    print(random.choice(list1))
