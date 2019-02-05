#! /usr/bin/env python

import os
import subprocess
import random

cmd_abstract = 'pandoc -s {} -o {}'
source_dirname = 'org'
target_dirname = 'md'


def get_modified_files():
    git_cmd = ['git', 'diff', '--name-only']
    output = subprocess.check_output(git_cmd).decode()
    files = output.split('\n')
    return files
        
def main():

    for fil in get_modified_files():
        if fil.find('org/') != -1:
            fil = fil.split('org/')[1]
            full_filename = os.path.join('org', fil)
            filename_without_extension = fil.split('.')[0]
            target_filename = os.path.join(target_dirname, filename_without_extension + '.md')
            cmd_concrete = cmd_abstract.format(full_filename, target_filename)
            print(cmd_concrete)
            os.system(cmd_concrete)
            random_filename = '/tmp/{}'.format(
                ''.join([str(random.randint(0, 9)) for i in range(20)]))
            os.system('python correct_inline_image.py {} {}'.format(target_filename,
                                                                    random_filename))


if __name__ == '__main__':
    main()
