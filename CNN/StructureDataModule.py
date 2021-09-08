import os
import re
from shutil import copy2


def getDataFileSplit(directory, data_files, file_split_type):
    files_dict = dict()
    class_dict = {1:'glass',  2:'paper', 3:'cardboard', 4:'plastic', 5:'metal', 6:'trash'}
    
    for file_name, split_type in zip(data_files, file_split_type):
        file = os.path.join(directory, file_name)
        files_dict[split_type] = []
        
        if os.path.isfile(file):
            with open(file) as f:
                lines = f.readlines()
                for line in lines:
                    split_line = line.partition(' ')
                    img = split_line[0]
                    class_id = int(re.sub(r'\n', '', split_line[-1]))
                    class_type = class_dict[class_id]
                    files_dict[split_type].append((img, class_type))
                               
    return files_dict



def createDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)       
    return



def setDirectoryTree(folders, split_types, root_path):   
    createDirectory(root_path)
    for main_directory in split_types:
        folder_path = os.path.join(root_path, main_directory)
        createDirectory(folder_path)
        
        for class_type in folders:
            class_path = os.path.join(folder_path, class_type)
            createDirectory(class_path)
    
    return



def copyFiles_to_tree(split_files, data_path, dst_path):
    for set_name, value_list in split_files.items():
        for img, class_type in value_list:
            origin_folder = os.path.join(data_path, class_type, img)
            dst_folder = os.path.join(dst_path, set_name, class_type)
            if not os.path.exists(os.path.join(dst_folder, img)):
                copy2(origin_folder, dst_folder)   
                
    print('Files moved succesfully!')
    return



def structure_data():
    origin_path = '.\dataset'
    dst_path = '.\input'
    data_path = os.path.join(origin_path, 'Garbage classification')

    data_files = ['one-indexed-files-notrash_train.txt', 'one-indexed-files-notrash_val.txt', 'one-indexed-files-notrash_test.txt']
    set_names = ['train_set', 'validation_set', 'test_set']
    class_types = os.listdir(data_path)

    split_files = getDataFileSplit(origin_path, data_files, set_names)
    setDirectoryTree(class_types, set_names, dst_path)
    copyFiles_to_tree(split_files, data_path, dst_path)
    return 