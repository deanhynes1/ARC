# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:31:32 2019

This methond / function for checking the index length of train and test input
"""
import json # Imported json python library

def check_train_test(file):
    """
    Function to Read the input file
    :param file: Input Json file
    :return: Index lengths of Train and test matrices
    """
    read_file = open(file, 'r')
    js = json.load(read_file)
    check_train_input = len(js['train'])
    check_test_input = len(js['test'])
    return {'Train Input': check_train_input, 'Test Input': check_test_input}
    read_file.close()
