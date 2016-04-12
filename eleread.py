import re
# function to parse the first line of text

def first_parse(line):
    data = line.split()
    return data

# call the functions and run through input file

def data_parse(file):
    element_data = {}
    iso_dict = {}
    for line in file:
        data = first_parse(line)
        if line[0] != ' ':
            ele_name = data[0]
            mm = data[1]
            atomic_number = data[2]
            density = data[3]
            num_isotopes = data[4]
            iso_dict = {}       # empty the isotope dictionary in preparation for next parse of isotopes
        elif line[0] == ' ':
            A = data[0]
            abund = data[1]
            iso_dict[A] = {'Abundance':abund}
        element_data[ele_name] = {'Molar Mass':mm,'Atomic Number':atomic_number,'Density':density,'Number of Isotopes':num_isotopes,'Isotope Data':iso_dict}
    return element_data
