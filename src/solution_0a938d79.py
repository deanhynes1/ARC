# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:19:43 2019

@author: dhynes


n solve which takes a single grid as input
and which returns a single grid.
"""
import operator
import numpy as np
from collections import defaultdict
import json


def check(*TEST):

    position = []
    position2 = []
    for i in range(len(TEST)):
        Targetinput = TEST[i]
        #print("   ")
        #print("in")
        #print(Targetinput)

        if  len(Targetinput) <= 11:#check the type of image input

            value2 = []
            #print(range(len(Targetinput)))
            for i in range(len(Targetinput)):
                for j in range(len(Targetinput[0])):
                    if Targetinput[i][j] > 0:
                        value = Targetinput[i][j]
                        #print(i,j)
                        value2.append(value)# the two values greater than 0
                        position.append(j)# the value positions

            space = (position[1]-position[0])#the space between them
            #print(space)


            for i in range(len(Targetinput)):
                for j in range(len(Targetinput)):
                    if Targetinput[i][j] >= 0:
                        if(space == 5):
                            Targetinput[i][position[0]] = value2[0]
                            Targetinput[i][position[0]+space] = value2[1]#pos 5 and 10
                            Targetinput[i][position[0]+2*space] = value2[0]
                            Targetinput[i][position[0]+3*space] = value2[1]
                            Targetinput[i][position[0]+4*space] = value2[0]



                                #Targetinput[i-1][j+4*space] = value1[0]
                        if(space == 2):
                            Targetinput[i][position[0]] = value2[0]
                            Targetinput[i][position[0]] = value2[0]
                            Targetinput[i][position[0]+space] = value2[1]
                            Targetinput[i][position[0]+2*space] = value2[0]
                            Targetinput[i][position[0]+3*space] = value2[1]
                            Targetinput[i][position[0]+4*space] = value2[0]
                            Targetinput[i][position[0]+5*space] = value2[1]
                            Targetinput[i][position[0]+6*space] = value2[0]
                            Targetinput[i][position[0]+7*space] = value2[1]
                            Targetinput[i][position[0]+8*space] = value2[0]
                            Targetinput[i][position[0]+9*space] = value2[1]
                        if(space == 3):
                            Targetinput[i][position[0]] = value2[1]
                            Targetinput[i][position[0]] = value2[0]
                            Targetinput[i][position[0]+space] = value2[1]
                            Targetinput[i][position[0]+2*space] = value2[0]
                            Targetinput[i][position[0]+3*space] = value2[1]
                            Targetinput[i][position[0]+4*space] = value2[0]
                            Targetinput[i][position[0]+5*space] = value2[1]





    ################################################################################
        else:
            #print("I am bigger than 11")

            values2 = []
            for i in range(len(Targetinput)):
                for j in range(len(Targetinput[0])):

                    if Targetinput[i-1][j-1] > 0:

                        value = Targetinput[i-1][j-1]

                        position2.append(i)
                        values2.append(value)


            space3 = position2[1]-position2[0]
            #print(space3)

            for i in range(len(Targetinput)):

                for j in range(len(Targetinput[0])):
                        Targetinput[position2[0]-1][j-1] = values2[0] #red
                        Targetinput[position2[1]-1][j-1] = values2[1]
                        Targetinput[(position2[0]-1)+2*space3][j-1] = values2[0] #red
                        Targetinput[(position2[1]-1)+2*space3][j-1] = values2[1]
                        Targetinput[(position2[0]-1)+4*space3][j-1] = values2[0] #red
                        if len(Targetinput[0]) == 9:
                            Targetinput[(position2[1]-1)+4*space3][j-1] = values2[1]
                            Targetinput[(position2[0]-1)+6*space3][j-1] = values2[0] #red
                            Targetinput[(position2[1]-1)+6*space3][j-1] = values2[1]
                            Targetinput[(position2[0]-1)+8*space3][j-1] = values2[0] #red




        #print(Targetinput)
        return Targetinput



def solve(t1):

    array = np.array(list(t1.items()))#put list into array
    TEST = []
    TESTOUT = []

    Targetinput1 = (array[0][1][0]["input"])
    Targetinput2 = (array[0][1][1]["input"])
    Targetinput3 = (array[0][1][2]["input"])
    Targetinput4 = (array[0][1][3]["input"])
    Targetinput0 = (array[1][1][0]["input"])
    TEST.append(Targetinput0)
    TEST.append(Targetinput1)
    TEST.append(Targetinput2)
    TEST.append(Targetinput3)
    TEST.append(Targetinput4)


    for i in range(len(TEST)):
        a = check(TEST[i])
        #TESTOUT.append('output')
        TESTOUT.append(a)

    #for i in range(len(TESTOUT)):
        #print(TESTOUT[i])



    with open('test.json', 'w') as json_file:
        json.dump(TESTOUT, json_file)

    with open('test.json') as json_file:
        readOut = json.load(json_file)
    #print(readOut)





    return TESTOUT
t1 = json.load(open(r"C:\Users\dhynes\Documents\GitHub\ARC\data\training\0a938d79.json"))
a = solve(t1)
## printing the output of the slove function.
for i in range(len(a)):
    print(" ")
    print(a[i])
