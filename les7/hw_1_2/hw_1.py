import json
import os


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def iter_tree(folders, path):
    for folder in folders:
        create_folder(os.path.join(path, folder))
        if folders[folder]:
            iter_tree(folders[folder], os.path.join(path, folder))


PATH = r'E:\git\first_course\first_course\les7\hw_1_2'
CONFIG = 'foldrs_tree.json'

with open(CONFIG, 'r') as f:
    iter_tree(json.load(f), PATH)



