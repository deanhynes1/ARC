# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:00:55 2019

@author: Mohammed Khalaquzzaman
ID:19239991
File Name = 'e179c5f4.json'
File location = '../src/e179c5f4.json
Solution File: solution_e179c5f4
"""
import json # Imported json python library
import numpy as np # Imported
import os as os
import argparse
from input_utility import check_train_test #Imported input utility to extact train & test length

# Primary keys of Input Json file
AREA = ['train', 'test']

# Parsing the Filepath as script argument
parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="Provide file path.")
args = parser.parse_args()
filename = args.file_path

'''
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
'''

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
    input_matrix = js[area][index]['input']
    original_output_matrix = js[area][index]['output']
    return input_matrix, original_output_matrix, file_name
    f.close()


def solve(input_matrix):
    """
    Function to calculate the Output matrix
    :param input_matrix: Input Matrix
    :return: Calculated Output matrix
    """
    INDEX = 0
    MAG = 1 # Initial magnitude to 
    new_matrix = []
    output_matrix = []

    ip_array = np.matrix(input_matrix)
    base_array = np.where(ip_array==0, 8, ip_array)

    base_matrix = base_array.tolist()

    for item in base_matrix[::-1]: # Iterating matix invertedly
        item[INDEX] = 1
        new_matrix.append(item)
        if INDEX == len(item) - 1:
            MAG = -1
        if INDEX == 0:
            MAG = 1
        INDEX = INDEX + MAG

    for item in new_matrix[::-1]: # Return to original matrix
        output_matrix.append(item)

    return output_matrix


def print_results(file_name, area, area_index, ip_matrix, org_op_matrix, calc_op_matrix):
    """
        Function to print results
        """
    print('=====Filename: {}, Area: {}, Index: {}====='.format(file_name, area, area_index + 1))
    print('=====', 'input', '=====')
    print("{}\n".format(np.matrix(ip_matrix)))
    print('=====', 'original output', '=====')
    print("{}\n".format(np.matrix(org_op_matrix)))
    print('=====', 'calculated output', '=====')
    print("{}\n".format(np.matrix(calc_op_matrix)))



def main():
    """
    Main execution workflow
    """
    len_dict = check_train_test(filename)
    train_length = len_dict['Train Input']
    test_length = len_dict['Test Input']
    print(len_dict)

    for area in AREA:
        if area == 'train':
            max_len = train_length
        elif area == 'test':
            max_len = test_length
        for index in range(max_len):
            ip_matrix, org_op_matrix, f_name = initialize(filename, index, area)
            calc_op_matrix = solve(ip_matrix)
            print_results(f_name, area, index, ip_matrix, org_op_matrix, calc_op_matrix)


if __name__ == "__main__":
    main()
