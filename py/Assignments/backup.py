#!/bin/python

import os, shutil

#copy all files from the source directory to the destination directory
def copy_files(source, destination):
    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        destination_path = os.path.join(destination, filename)
        shutil.copy(source_path, destination_path)  

#main function
if __name__ == '__main__':
    source = input("Enter the source directory: ")
    destination = input("Enter the destination directory: ")
    copy_files(source, destination)

