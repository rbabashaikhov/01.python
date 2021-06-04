import os

my_folders = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
def create_folders(folders):
    for folder in folders.keys():
        for subfolder in folders[folder]:
            dir_path = os.path.join(folder, subfolder)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

create_folders(my_folders)
