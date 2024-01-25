#!/bin/python
import json, os

#program should read a configuration file and show error if its not found, If present read the contents and  store it in list
def read_configuration(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            return f.read().splitlines()
    else:
        raise FileNotFoundError
    
#function read the list and put in json format
def write_json(filename, data):
    with open(filename, 'w') as f:
        return json.butify(data, indent=2)
    

#main function
if __name__ == '__main__':
    filename = 'config.txt'
    data = read_configuration(filename)
    write_json('config.json', data)