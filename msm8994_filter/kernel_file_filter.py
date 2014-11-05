#!/usr/bin/python

import sys

kern_files = []

def main_func(log_filename):
    log_fp = open(log_filename)
    for line in log_fp:
        Strs = line.split(' ')
        try:
            i = Strs.index("#warning")
            path_with_magic = Strs[i+1]
        except:
            continue
        
        Strs = path_with_magic.strip().split('_',4)
        if(Strs[0] == 'eecbfb859094a362907dfb2f2cd3a8c8'):
            path=Strs[-1].strip()
        else:
            continue
            
        try:
            kern_files.index(path)
        except:
            kern_files.append(path)
    log_fp.close()

    compiled_files = open('compiled_files.txt','w')
    for line in kern_files:
        compiled_files.write("%s\n" %(line.strip()))
    compiled_files.close()
    
if __name__ == "__main__":
    print(sys.argv)
    main_func(sys.argv[1])
