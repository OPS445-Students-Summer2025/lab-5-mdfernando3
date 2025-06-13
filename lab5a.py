#!/usr/bin/env python3
# Author ID: mdfernando3

def read_file_string(file_name):
    f = open(file_name, 'r')
    contents = f.read()
    f.close()
    return contents


def read_file_list(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    new_lines = []
    for line in lines:
        new_lines.append(line.strip())
    return new_lines    

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
