import sys
import time
import os 

#list files with the given directory
#this function is important for searching
def list_files(path):
    result = []
    directory = os.scandir(path)

    for file in directory:
        #if file.is_dir() or file.is_file():
        if file.is_dir():
            #print(file.name)
            result.append(file.name)

    directory.close()
    return result

#list files with the given directory
#this function is important for listing files
def list_file(path):
    result = []
    directory = os.scandir(path)

    for file in directory :
        if file.is_file():
            result.append(file.name)
    
    directory.close()
    return result

def depth_first_search(path):
    stack = []
    visited = []
    root = path
    current_path = root
    stack.append(current_path)

    pyFile_list = []

    while len(stack) > 0:
        current_path = stack.pop()
        file_list = list_files(current_path)
        if current_path not in visited:
            visited.append(current_path)
            #print(current_path) ####################################
            for file in list_file(current_path): 
                print(file)    #####################################
                pyFile_list.append(current_path +"/"+file)
                #TODO:
                #more features can be integrated after this line in the if
                
                #this is just a testing of listing all functions in all files
                # print(ProcessPy.list_defs(current_path+"/"+file))

        for n in file_list:
            if n not in visited:
                stack.append(current_path + "/" + n)

    return pyFile_list


depth_first_search("C:/Users/ygooi/Desktop/Arizona Trip")