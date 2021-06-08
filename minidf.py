#!/usr/bin/env python3
import argparse
import shutil
import os

def humanReadable(stat):
    htotal = humansize(stat.total)
    hfree = humansize(stat.free)
    hused = humansize(stat.used)
    return htotal, hfree, hused

suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def calc(paths):
    parser = argparse.ArgumentParser()
    parser.add_argument("-hr", "--hrflag", action="store_true", help="Gives result in human readable format.")
    parser.add_argument("paths", nargs = '*', help="paths of files separated by space")
    args = parser.parse_args() 

    paths = args.paths
    if not paths:
        #add current dir 
        paths.append(os.getcwd())

    total, free, used = "", "", ""
    print(paths)
    for path in paths:
        stat = shutil.disk_usage(path)
        if args.hrflag:
           total, free, used = humanReadable(stat)

        else:
            total, free, used = str(stat.total), str(stat.free), str(stat.used)
        return total, free, used 
        print(f"{path} : Total Space - {total}, Free Space - {free}, Used Space - {used}")
        
if __name__ == "__main__":
    calc(paths)
