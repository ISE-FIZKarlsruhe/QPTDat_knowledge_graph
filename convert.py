#!/usr/bin/env python3

import sys
import getopt
import rdflib


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    graph = rdflib.Graph()
    graph.parse(inputfile, format="turtle")
    graph.serialize(destination=outputfile, format='nt')

if __name__ == "__main__":
    main(sys.argv[1:])
