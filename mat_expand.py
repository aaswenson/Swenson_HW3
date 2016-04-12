# This script will take a material input file and generate a material
# composition in nuclide abundances rather than elemental mass fractions

import re
from matread import data_par
from eleread import data_parse

mat_dat = open('matlib.std')
ele_dat = open('elelib.std')

ele_library = data_parse(ele_dat)
mat_library = data_par(mat_dat)

def number_densities(ele_library, mat_library):
    number_densities = {}
    sub_dat = {}
    for key in mat_library:
        rho = mat_library[key]['Density']
        for subsubkey in mat_library:
            mol_mass = ele_library[subsubkey]['Molar Mass']
            atom_number = mat_library[key]['Composition Data'][subsubkey]['Atomic Number']
            w_o = mat_library[key]['Composition Data'][subsubkey]['Mass Fraction']
            for subsubsubkey in ele_library[subsubkey]['Isotope Data'][subsubsubkey]:
                ID = int(subsubsubkey)+ 1000*int(atom_number)
                a_o = ele_library[subsubkey]['Isotope Data'][subsubsubkey]
                N_i = float(rho)*float(a_o)*float(w_o)/float(mol_mass)
                sub_dat[ID] = N_i
                
        number_densities[key] = sub_dat
    return number_densities

expand = number_densities(ele_library,mat_library)
print(expand)

        
