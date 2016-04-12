# This script parses a material database

import re 

file = open('matlib.std')

# function to parse through the first line of text

def first_parse(line):
    data = line.split()
    return(data)

def data_par(line):   
    material_dat = {} 
    for line in file:
        data = first_parse(line)  
        if len(data[0]) > 2:
            alloy = data[0]
            density = data[1]
            num_of_elements = data[2]
            comp_dat = {}
        else:
            element = data[0]
            mass_frac = data[1]
            atomic_number = data[2]
            comp_dat[element]={'Atomic Number':atomic_number,'Mass Fraction':mass_frac}
        material_dat[alloy]={'Density':density,'Number of Elements':num_of_elements,'Composition Data':comp_dat}


