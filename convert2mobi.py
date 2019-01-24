#!/usr/bin/env python3

import glob
import os
import subprocess
import argparse
import sys

def mkdir(dir):
    if dir == None:
        return None
    # endif
    if not os.path.isdir(dir):
        os.makedirs(dir, exist_ok=True)
    # endif
# enddef

def rp(dir):
    if dir == None:
        return None
    # endif
    if dir[0] == '.':
        return os.path.normpath(os.getcwd() + '/' + dir)
    else:
        return os.path.normpath(os.path.expanduser(dir))
# enddef

def chkdir(dir):
    if not os.path.isdir(dir):
        print('{} does not exist !!'.format(dir))
        sys.exit(-1)
    # endif
# enddef

def convert(src_dir, dst_dir):
    src_dir = rp(src_dir)
    dst_dir = rp(dst_dir)

    file_list = glob.glob('/mnt/sdb1/data/ebooks/**/*.epub', recursive=True)
    mkdir(dst_dir)
    ctr = 1
    for file_t in file_list:
        dst_file = '{}/{}.mobi'.format(dst_dir, os.path.splitext(os.path.basename(file_t))[0])
        print('[{:<4}/{:<4}] Converting {}'.format(ctr, len(file_list), file_t))
        subprocess.call(['ebook-convert', file_t, dst_file])
        ctr = ctr + 1
    # endfor
# enddef

if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    parser.add_argument('--in_dir',   help='Input dir.',      type=str, default=None)
    parser.add_argument('--out_dir',  help='Output dir.',      type=str, default=None)
    args    = parser.parse_args()

    if args.__dict__['in_dir'] == None or args.__dict__['out_dir'] == None:
        print('All options are mandatory.Please use --help for more information.')
        sys.exit(-1)
    # endif

    convert(args.__dict__['in_dir'], args.__dict__['out_dir'])
# endif
