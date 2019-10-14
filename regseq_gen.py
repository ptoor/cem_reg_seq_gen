import sys
import argparse
def get_reglist(file_handle):
    reglist = []
    for line in file_handle:
        reglist.append(line.split(' ')[0].lower())
    return(reglist)

regs = get_reglist(open(sys.argv[1], "r"))
print(regs)