import json
import os


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def create_file(path):
    open(path, 'w').close()


def iter_tree(folders, path):
    for folder in folders:
        if folders[folder] and type(folders[folder]) == dict:
            create_folder(os.path.join(path, folder))
            iter_tree(folders[folder], os.path.join(path, folder))
        elif folders[folder] == 'file':
            create_file(os.path.join(path, folder))


PATH = r'E:\git\first_course\first_course\les7\hw_1_2'
CONFIG = 'foldrs_tree_2.json'

with open(CONFIG, 'r') as f:
    iter_tree(json.load(f), PATH)
