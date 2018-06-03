This is a script that takes an .txt file with the following parameters and saves a graph of the simulated planets' final positions on a trillion by trillion metre plot.

The file contains information for each planet one planet per line with its initial properties (mass, x position, y position, x velocity, y velocity) separated by spaces
mass in kg, position in m, velocity in m/s

Ex:
1.989e30 5e11 5e11 0 0
5.972e24 5e11 6.496e11 30000 0


The script takes 4 arguments:

 1) '--input_filename'   - the directory of your input file
 2) '--output_directory' - the directory of your output graph
 3) '--delta_t'          - what final time (in seconds) you want the script to calculate
			   to and the graph to be showing
 4) '--timestep'         - also in seconds, this is the timestep used for physics
			   calculations. The smaller this number is, the more accurate the
			   result will be, but the script will take longer to run