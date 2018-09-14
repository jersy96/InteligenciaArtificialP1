# from copy import deepcopy

def file_to_matrix(path):
    f = open ( path , 'r')
    m = [[int(num) for num in line.split(',')] for line in f ]
    return m
