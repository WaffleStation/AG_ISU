#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:04:09 2018

@author: arielgans
"""

import argparse
import math
import matplotlib.pyplot as plt


def newton(planets, n):
    #takes the list of planets and the index of the planet in question.
    #Returns the force in the x dimension and the force in the y dimension
    
    fx = fy = 0
    
    for i in range(len(planets)):
        if i != n: #I guess this isn't technically necessary but it helps speed it up a bit
            dx = planets[i][1] - planets[n][1] #diff in x
            dy = planets[i][2] - planets[n][2] #diff in y
            if dx == 0 and dy >= 0: #If statements to hardcode angles 90˚ and 270˚ where arctan can't be calculated
                angle = math.pi / 2
            elif dx == 0:
                angle = ( 3 * math.pi ) / 2
            else:
                angle = math.atan2( dy, dx )
            
            ftot = ( (6.6e-11)*(planets[i][0]*planets[n][0]) ) / ( (dx*dx)+(dy*dy) ) #Newton's equation
            
            fx += math.cos(angle) * ftot
            fy += math.sin(angle) * ftot
    
    return fx, fy


def velocity(planet, fx, fy, dt):
    #takes planet entry in planets, the force variables and the timestep
    #returns horizontal and vertical velocity
    
    vx = planet[3] #init vs
    vy = planet[4]
    
    #final vs
    vx += ( fx / planet[0] ) * dt  #acceleration * timestep
    vy += ( fy / planet[0] ) * dt
    
    return vx, vy


def iterate(planets, dt):
    #takes the list of planets and the timestep
    #edits lists with new displacements and velocities then returns 0
    
    for item in planets:
        force = newton(planets, planets.index(item))
        item[3:5] = velocity(item, force[0], force[1], dt)
        item[1] += item[3] * dt
        item[2] += item[4] * dt


def main():
    parser = argparse.ArgumentParser(description = "Generates graph displaying position of inputted planets after ∆t")
    parser.add_argument('--input_filename',required = True,type = str, dest = "ifile", 
                        help = "The planets are inputted through a file with one planet per line and its initial properties (mass, x position, y position, x velocity, y velocity) separated by spaces\nmass in kg, position in m, velocity in m/s\nEx:\n1.989e30 5e8 5e8 0 0\n5.972e24 5e8 6.496e8 30 0")
    parser.add_argument('--output_directory',required = True, type = str, dest = "odir",
                        help = "Specify an output directory including name and extension")
    parser.add_argument('--delta_t',required = True, type = int, dest = "deltat",
                        help = "Change in time (seconds)")
    parser.add_argument('--timestep',required = True, type = int, dest = "ts",
                        help = "Timestep (seconds). The smaller, the more accurate but the longer the run time.")
    
    args = parser.parse_args()
    
    planets = []
    
    with open(args.ifile) as f_i:
        for line in f_i:
            linelist = line.split()
            if len(linelist) == 5:
                planets.append([ float(x) for x in linelist ])
            else:
                print("Input formatting error!")
                return
            
    for i in range(int(args.deltat / args.ts)): # do the calculating
        iterate(planets, args.ts)
    
    xaxis = [] # making data
    yaxis = []
    for x in planets:
        xaxis.append(x[1])
        yaxis.append(x[2])
    
    plt.plot(xaxis, yaxis, 'ro') # add data to plot
    
    plt.figure(1, figsize=[10,10]) # æsþetiques
    plt.xlim([0,1e12])
    plt.ylim([0,1e12])
    plt.xlabel('x displacement (m)')
    plt.ylabel('y displacement (y)')
    plt.suptitle(repr(len(planets)) + '-Body Simulation')
    #plt.title('∆t = {:.0e}'.format(args.deltat))
    
    plt.savefig(args.odir) # saving
    
    return

if __name__ == "__main__":
    main()