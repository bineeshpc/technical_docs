#! /usr/bin/env python

import os

cmd_abstract = 'pandoc -s {} -o {}'
source_dirname = 'org'
target_dirname = 'md'

for fil in os.listdir(dirname):
    full_filename = os.path.join(source_dirname, fil)
    filename_without_extension = fil.split('.')[0]
    target_filename = os.path.join(target_dirname, filename_without_extension + '.md')
    cmd_concrete = cmd_abstract.format(full_filename, target_filename)
    os.system(cmd_concrete)
