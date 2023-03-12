#!/usr/bin/env python3
# coding: utf-8

__doc__ = """
Multext-EAST map generator
"""

import argparse
import json
import os
import sys


def parse_args(arguments):
    parser = argparse.ArgumentParser(usage="Multext-EAST Map Generator")
    parser.add_argument('-i', '--input-file',
        help="Input file with mapping elements in JSON format", required=True)
    parser.add_argument('-o', '--output-file', default=sys.stdout,
        help="Output file", required=False)
    return parser.parse_args(arguments)


def get_desc(str, delim):
    l = str.split()
    return delim.join(x for x in l if x.find("DUMMY") == -1)


def gen_tags(l):
    for i0 in l[0]:
        for i1 in l[1]:
            for i2 in l[2]:
                for i3 in l[3]:
                    for i4 in l[4]:
                        for i5 in l[5]:
                            for i6 in l[6]:
                                for i7 in l[7]:
                                    for i8 in l[8]:
                                        for i9 in l[9]:
                                            for i10 in l[10]:
                                                for i11 in l[11]:
                                                    for i12 in l[12]:
                                                        for i13 in l[13]:
                                                            for i14 in l[14]:
                                                                t = f"{i0[0]}{i1[0]}{i2[0]}{i3[0]}{i4[0]}{i5[0]}"
                                                                t = f"{t}{i6[0]}{i7[0]}{i8[0]}{i9[0]}{i10[0]}{i11[0]}"
                                                                t = f"{t}{i13[0]}{i14[0]}"
                                                                d = f"{i1[1]} {i2[1]}"
                                                                d = f"{d} {i3[1]} {i4[1]} {i5[1]} {i6[1]} {i7[1]} {i8[1]}"
                                                                d = f"{d} {i9[1]} {i10[1]} {i11[1]} {i12[1]} {i13[1]}"
                                                                d = f"{d} {i14[1]}"
                                                                tstrp = t.rstrip('-')
                                                                dstr = get_desc(d, " ")
                                                                print(tstrp, dstr)


# Generates multext map
def gen_word_type_lists(inmap):
    for (word_type, word_type_dict,) in inmap.items():
        if word_type == 'Metadata':
            continue
        listag = (list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list())
        for spec in word_type_dict["specification"]:
            pos = spec["position"]
            for value in spec["values"]:
                listag[pos].append((value["code"], f"{spec['attribute']}={value['value']}"))
        for index in range(15):
            if len(listag[index]) == 0:
                listag[index].append(('-', ''))
        gen_tags(listag)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if not os.path.exists(args.input_file):
        print(f"ERROR: Input file '{args.input_file}' does not exist.")
        exit(1)
    with open(args.input_file, 'r') as file:
        inmap = json.load(file)
        gen_word_type_lists(inmap)
