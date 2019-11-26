# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:00:55 2019

@author: Mohammed Khalaquzzaman
ID:19239991
"""

import json # Imported json python library
import numpy as np # Imported numpy as np
import os as os # Import os python libray for using file path 
import argparse # Imported argparse for parsing th file path

# INDEX = [0, 1]
# Primary key of Input Json file
AREA = 'train'
# filename = 'a61f2674.json'

# Parsing the Filepath as script argument
parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="Provide file path.")
args = parser.parse_args()
filename = args.file_path


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


def initialize(file, index, area='train'):
    """
    Function to read the input file and fetch Input and Original Output matrices
    :param file: Input Json File
    :param index: Current Index value
    :param area: Area
    :return: Input matrix, Original Output matrix, File base name
    """
    f = open(file, 'r')
    file_name = os.path.basename(f.name)
    js = json.load(f)
    input_matrix = np.matrix(js[area][index]['input'])
    # print("Original Input Matrix\n\n", input_matrix)
    original_output_matrix = np.matrix(js[area][index]['output'])
    # print("\nOriginal Output Matrix\n\n", original_output_matrix)
    return input_matrix, original_output_matrix, file_name
    f.close()


def solve_a61f2674_task(input_matrix):
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
    # print(tallest_index, shortest_index)

    # Creating new matrix with zeros
    new_matrix = np.zeros(shape=input_matrix.shape, dtype=int)
    
    # Assign tallest and shortest index to new matrix
    new_matrix[:, tallest_index] = input_matrix[:, tallest_index].T
    new_matrix[:, shortest_index] = input_matrix[:, shortest_index].T
    new_matrix[:, tallest_index][new_matrix[:, tallest_index] > 0] = 1
    new_matrix[:, shortest_index][new_matrix[:, shortest_index] > 0] = 2
    return new_matrix, tallest_index, shortest_index


def print_results(file_name, area, area_index, ip_matrix, org_op_matrix, op_matrix,
                  tall_index, short_index):
    """
    Function to print results
    """
    print('=====Filename: {}, Area: {}, Index: {}====='.format(file_name, area, area_index+1))
    print('=====', 'input', '=====')
    print("{}\n".format(ip_matrix))
    # print('Shortest Index: {}, Tallest Index: {}'.format(short_index, tall_index))
    print('=====', 'original output', '=====')
    print("{}\n".format(org_op_matrix))
    print('=====', 'calculated output', '=====')
    print("{}\n".format(op_matrix))


def main():
    """
    Main execution workflow
    """
    len_dict = check_train_test(filename)
    train_length = len_dict['Train Input']
    print(len_dict)
    for index in range(train_length):
        ip_matrix, org_op_matrix, f_name = initialize(filename, index, AREA)
        op_matrix, tl_ix, sh_ix = solve_a61f2674_task(ip_matrix)
        print_results(f_name, AREA, index, ip_matrix, org_op_matrix, op_matrix, tl_ix, sh_ix)


if __name__ == "__main__":
    main()
