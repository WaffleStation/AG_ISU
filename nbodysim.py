#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:04:09 2018

@author: arielgans
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description = "Generates graph displaying position of inputted planets after ∆t")
    parser.add_argument('--input_filename',required = True,type = str, dest = "ifile", 
                        help = "The planets are inputted through a file with one planet per line and its initial properties (mass, x position, y position, x velocity, y velocity) separated by spaces\nmass in kg, position in km, velocity in km/s\nEx:\n1.989e30 5e8 5e8 0 0\n5.972e24 5e8 6.496e8 30 0")
    parser.add_argument('--output_directory',required = True, type = str, dest = "odir",
                        help = "Specify an output directory including name and extension")
    parser.add_argument('--delta_t',required = True, type = int, dest = "delat",
                        help = "Change in time (seconds)")
    parser.add_argument('--timestep',required = True, type = int, dest = "ts",
                        help = "Timestep (seconds). The smaller, the more accurate but the longer the run time.)
    
    args = parser.parse_args()
    
    return

if __name__ == "__main__":
    main()