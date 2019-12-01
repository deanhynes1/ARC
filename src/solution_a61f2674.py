# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:00:55 2019

@author: Mohammed Khalaquzzaman
ID:19239991
File Name = a61f2674.json
File location = C:\MAO\CT5148\ARC\data\training\a61f2674.json
Solution File: solution_a61f2674.py

"""

import json # Imported json python library
import numpy as np # Imported numpy as np
import os as os # Import os python libray for using file path 
import argparse # Imported argparse for parsing th file path
from input_utility import check_train_test #Imported input utility to extact train & test length

# INDEX = [0, 1]
# Primary test keys of Input Json file
AREA = 'test'

# Parsing the Filepath as script argument
parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="Provide file path.")
args = parser.parse_args()
filename = args.file_path

def initialize(file, index, area='test'):
    """
    Function to read the input file and fetch Input and Original Output matrices
    :param file: Input Json File
    :param index: Current Index value
    :param area: Area
    :return: Input matrix, Original Output matrix, File base name
    """
    f = open(file, 'r')
    file_name = os.path.basename(f.name)
    load_json_file = json.load(f) # load json file 
    input_matrix = np.matrix(load_json_file[area][index]['input'])
    # print("Original Input Matrix\n\n", input_matrix)
    original_output_matrix = np.matrix(load_json_file[area][index]['output'])
    # print("\nOriginal Output Matrix\n\n", original_output_matrix)
    return input_matrix, original_output_matrix, file_name
    f.close()


def solve(input_matrix):
    """
    Function to calculate the Output matrix
    :param input_matrix: Input Matrix
    :return: Calculated Output matrix, Tallest Index, Shortest Index
    """
    tallest_val = 0
    tallest_index = None

    shortest_val = 10
    shortest_index = None
    for index in range(input_matrix.shape[1]):
        non_zero = sum((1 for x in input_matrix[:, index] if x > 0))
        if non_zero > tallest_val:
            tallest_val = non_zero
            tallest_index = index
        if non_zero > 0 and non_zero < shortest_val:
            shortest_val = non_zero
            shortest_index = index


    # Creating new matrix with zeros
    new_matrix = np.zeros(shape=input_matrix.shape, dtype=int)
    
    # Assign tallest and shortest index to new matrix
    new_matrix[:, tallest_index] = input_matrix[:, tallest_index].T
    new_matrix[:, shortest_index] = input_matrix[:, shortest_index].T
    new_matrix[:, tallest_index][new_matrix[:, tallest_index] > 0] = 1
    new_matrix[:, shortest_index][new_matrix[:, shortest_index] > 0] = 2
    return new_matrix, tallest_index, shortest_index


def print_results(file_name, calc_output_matrix, tallest_index, shortest_index):
    """
    Function to print results without bracket 
    """
    print(str(np.matrix(calc_output_matrix)).replace(']',' ').replace('[',' '))


def main():
    """
    Main execution workflow for Test Input
    """
    len_dict = check_train_test(filename)
    test_length = len_dict['Test Input']
            
    for index in range(test_length):
        input_matrix, org_output_matrix, f_name = initialize(filename, index, AREA)
        calc_output_matrix, tallest_index, shortest_index = solve(input_matrix)
        print_results(f_name, calc_output_matrix, tallest_index, shortest_index)


if __name__ == "__main__":
    main()
