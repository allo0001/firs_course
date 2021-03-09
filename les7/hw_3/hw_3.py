import json
import os
from shutil import copyfile


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


PATH = r'C:\Users\loktionov\Documents\GitHub\firs_course\les7\hw_3'
CONFIG = 'foldrs_tree_2.json'

with open(CONFIG, 'r') as f:
    iter_tree(json.load(f), PATH)

mp_path = os.path.join(PATH,'my_project')
create_folder(os.path.join(mp_path, 'templates'))
for root, dirs, files in os.walk(mp_path):
    if files:
        folder_name = os.path.split(root)[1]
        if os.path.split(root)[0] != os.path.join(mp_path, 'templates'):
            for file in files:
                if file.endswith('.html'):
                    create_folder(os.path.join(mp_path, 'templates', folder_name))
                    copyfile(os.path.join(root, file), os.path.join(mp_path, 'templates',folder_name, file))
