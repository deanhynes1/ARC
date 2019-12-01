# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:00:55 2019

@author: Mohammed Khalaquzzaman
ID:19239991
Task Json file Name = 'e179c5f4.json'
File location = 'C:\MAO\CT5148\ARC\data\training\e179c5f4.json'
Solution File: 'solution_e179c5f4'
Solve the task which has a single grid input blue color and which returns 
one diagonal outuput with blue color and remaining all grids will be light
blue color.
"""
import json # Imported json python library
import numpy as np # Imported numpy as np
import os as os # Import os python libray for using file path 
import argparse # Imported argparse for parsing th file path
from input_utility import check_train_test #Imported input utility to extact train & test length


# Primary test keys of Input Json file
AREA = ['train', 'test']

# Parsing the Filepath as script argument
parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="Provide file path.")
args = parser.parse_args()
filename = args.file_path


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
    load_json_file = json.load(f)
    input_matrix = load_json_file[area][index]['input']
    original_output_matrix = load_json_file[area][index]['output']
    return input_matrix, original_output_matrix, file_name
    f.close()
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
'''    
def solve(input_matrix):
    """
    Function to calculate the Output matrix
    :param input_matrix: Input Matrix
    :return: Calculated Output matrix
    """
    INDEX = 0
    MAG = 1
    new_matrix = []
    output_matrix = []

    input_array = np.matrix(input_matrix)
    base_array = np.where(input_array==0, 8, input_array)

    base_matrix = base_array.tolist()

    for item in base_matrix[::-1]:
        item[INDEX] = 1
        new_matrix.append(item)
        if INDEX == len(item) - 1:
            MAG = -1
        if INDEX == 0:
            MAG = 1
        INDEX = INDEX + MAG

    for item in new_matrix[::-1]:
        output_matrix.append(item)

    return output_matrix


def print_results(f_name, area, index, ip_matrix, org_op_matrix, calc_op_matrix):
    """
    Function to print results without bracket
    """
    print(str(np.matrix(org_op_matrix)).replace(']',' ').replace('[',' '))
    print("\n".format(str(np.matrix(calc_op_matrix)).replace(']',' ').replace('[',' ')))



def main():
    """
    Main execution workflow for train and test input
    """
    len_dict = check_train_test(filename)
    train_length = len_dict['Train Input']
    test_length = len_dict['Test Input']
    #print(len_dict)
    
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
