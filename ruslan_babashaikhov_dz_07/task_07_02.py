import os
from shutil import copyfile
from collections import defaultdict

def copy_files(src, tgt):

    for root, dirs, files in os.walk(src):
        for file in files:
            ext = file.rsplit('.', maxsplit = 1)[1].lower()
            if ext == 'html':
                if not os.path.exists(os.path.join(tgt, 'templates', root.split('/')[-2])):
                    os.makedirs(os.path.join(tgt, 'templates', root.split('/')[-2]))
                copyfile(os.path.join(root, file), os.path.join(tgt, 'tamplates', root.split('/')[-2], file))

copy_files('my_project', 'my_templates')
