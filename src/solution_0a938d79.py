# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:19:43 2019

@author: Dean Hynes
Student 09101907
Class Maters in A.I NUIG


n solve which takes a single grid as input
and which returns a single grid.
"""

import numpy as np #Import np for array operations
from collections import defaultdict #Import from collections import defaultdict for dictionary use
import os # Import os to use pat to file
import argparse #import argparse to use when running the code to get the path to the file
import json #Import json to use the python json lib
import sys
localfile = json.load(open(r"C:\Users\dhynes\Documents\GitHub\ARC\data\training\0a938d79.json"))

def solveInput(*TEST):
    '''
    function def::
    The solveInput(*TEST) function takes the input grids as arrays,
    checks where the colured squares and takes thier position.
    check the spaces between both squares in the grid.
    Add a stipped effect to the ouput grid with the colurs and the spaces between them,
    vertically and horizontally where applicable all the way to the end each input grid.


    '''
    position = []
    position2 = []
    for i in range(len(TEST)):
        Targetinput = TEST[i]
        #print("   ")
        #print("in")
        #print(Targetinput)

        if  len(Targetinput) <= 11:#check the imput grid is vertical or horizontal in this folder

            value2 = []
            #print(range(len(Targetinput)))
            for i in range(len(Targetinput)):## loop through the grid and take the colour value and position
                for j in range(len(Targetinput[0])):
                    if Targetinput[i][j] > 0:# if great than zero, this is a colour take the value and position
                        value1 = Targetinput[i][j]
                        #print(i,j)
                        value2.append(value1)# the two values greater than 0
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

def solve_0a938d79(t1 = localfile):

    '''
    function def::
    solve_0a938d79(t1) takes the input file and convers to array.
    if not file is given on the cmd line solve works on the local file on my machine.



    '''
    #t1 = json.load(open(t1,'r'))
    array = np.array(list(t1.items()))#put list into array
    TEST = [] # create container of the test inputs to be solved.
    TESTOUT = []# create container to send out the solved tests.
    # quick way to access the data and take each test as a septerated inputs
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
        a = solveInput(TEST[i])
        #TESTOUT.append('output')
        TESTOUT.append(a)




    with open('test.json', 'w') as json_file:#open a json file and fill with the answers.
        json.dump(TESTOUT, json_file)

    with open('test.json') as json_file:
        readOut = json.load(json_file)
    #print(readOut)





    return TESTOUT

def main():#Added main for tidy up
    '''
    function def::
    Main function allows to run on cmd line with the path to test file as an argument
    On cmd line check the arguement len is greater than 1, this means a path to the test file has been attached



    '''
    # Pass the path of the file as an argument
    arguments = len(sys.argv) - 1
    parse = argparse.ArgumentParser()
    parse.add_argument("Path_to_file", help="Provide file path.")
    position = 1
    if (arguments >= position): #check arguements are given at cmd line and pick up the path to the file
        args = parse.parse_args()
        filename = args.Path_to_file
        #print("I ran")
        filename = json.load(open(filename,'r'))
        a = solve_0a938d79(filename)

    a = solve_0a938d79()#if no path to file is given on cmd run default on localfile.
    print("you added not path to cmd line localfile run")
        ## printing the output of the slove function.
    for i in range(len(a)):#Put space between ouput arrays
        print(" ")
        print(a[i])

if __name__=="__main__":#execute only if run as a script
    main()
