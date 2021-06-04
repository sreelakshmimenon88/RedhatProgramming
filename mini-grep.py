#!/usr/bin/env python3
import argparse
import re

def printOutput(lines, args):
    for i,line in enumerate(lines): 
        if re.search(args.pattern, line):
            if args.qflag:
                print(line)
            else:
                print(f"Line {i+1} : {line}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--qflag", action="store_true", help="hide line numbers of lines that match given pattern.")
    parser.add_argument("-e", "--eflag", action="store_true", help="empty flag.")
    parser.add_argument("pattern", help="pattern to match with file lines")
    parser.add_argument("files", nargs = '*', help="paths of files separated by space")
    args = parser.parse_args()

    filepaths = args.files
    lines = []

    if not filepaths:
        filepaths = input('Enter path of the files:').split()
	
    for filepath in filepaths:
        with open(filepath) as f:
            lines = f.readlines()
            print('File - ' + filepath)
        printOutput(lines, args)