# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:19:43 2019

@author: dhynes


n solve which takes a single grid as input
and which returns a single grid. 
"""

import json
from structshape import structshape
print("input-output grid pairs which demonstrate, given an input grid, what the correct output grid would be.")
t1 = json.load(open("Test1.json"))
t2 = json.load(open("Test2.json"))
t3 = json.load(open("Test3.json"))

print(t1.keys())

#print(t2)
#print(type(t1))
#d[0].keys()
#print(structshape(t1))

def solve_test1(t1):
    
    
    
    
    
    return gridAns


def find_colour(_val):
    # Colour value constants
    _colours = {"blue": [0.0, 0.0, 1.0],
                "green": [0.0, 1.0, 0.00],
                "yellow": [1.0, 1.0, 0.0],
                "red": [1.0, 0.0, 0.0]}

    # Map the value to a colour
    _colour = [0, 0, 0]
    if _val > 30:
        _colour = _colours["red"]
    elif _val > 20:
        _colour = _colours["blue"]
    elif _val > 10:
        _colour = _colours["green"]
    elif _val > 0:
        _colour = _colours["yellow"]

    return tuple(_colour)
#print(t1['test'])
#print(t1['train'])
print(t1.keys())
#find_colour(int(t2)