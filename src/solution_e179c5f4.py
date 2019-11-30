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
import numpy as np # Imported numpy as np
import os as os # Imported operating system as os
import argparse
from input_utility import check_train_test #Imported input utility to extact train & test length

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
    load_json_file = json.load(f)
    input_matrix = load_json_file[area][index]['input']
    original_output_matrix = load_json_file[area][index]['output']
    return input_matrix, original_output_matrix, file_name
    f.close()


def solve(input_matrix):
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


def print_results(file_name, calc_output_matrix):
    """
    Function to print results without bracket
    """
    print(str(np.matrix(calc_output_matrix)).replace(']',' ').replace('[',' '))


def main():
    """
    Main execution workflow for test input
    """
    len_dict = check_train_test(filename)
    test_length = len_dict['Test Input']
    #print(len_dict)

    for index in range(test_length):
        input_matrix, org_op_matrix, f_name = initialize(filename, index, AREA)
        calc_output_matrix = solve(input_matrix)
        print_results(f_name, calc_output_matrix)


if __name__ == "__main__":
    main()
