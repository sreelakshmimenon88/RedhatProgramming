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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-hr", "--hrflag", action="store_true", help="hide line numbers of lines that match given pattern.")
    parser.add_argument("paths", nargs = '*', help="paths of files separated by space")
    args = parser.parse_args() 

    paths = args.paths
    if not paths:
        #add current dir 
        paths.append(os.getcwd())

    total, free, used = "", "", ""

    for path in paths:
        stat = shutil.disk_usage(path)
        if args.hrflag:
           total, free, used = humanReadable(stat)

        else:
            total, free, used = str(stat.total), str(stat.free), str(stat.used)

        print(f"{path} : Total Space - {total}, Free Space - {free}, Used Space - {used}")
    


