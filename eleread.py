import re
# function to parse the first line of text

def first_parse(line):
    ele_name = line[0:2]
    ele_name = ele_name.strip()
    mm = line[9:20]
    z = line[23:24]
    z = z.strip()
    density = line[31:42]
    num_isotopes = line[46:47]
    num_isotopes = num_isotopes.strip()
    return [ele_name,mm,z,density,num_isotopes]

# function to parse the isotope lines

def iso_parse(line):
    line = line.strip()
    print(line)
    A = line[0:2]
    A = A.strip()
    abund = line[9:20]
    return [A,abund]

# call the functions and run through input file

def data_parse(file):
    element_data = {}
    for line in file:
        if line[0] != ' ':
            a = first_parse(line)
            iso_dict = {}       # empty the isotope dictionary in preparation for next parse of isotopes
        elif line[0] == ' ':
            b = iso_parse(line)
            iso_dict[b[0]] = {'Abundance':b[1]}
            print(iso_dict)
        element_data[a[0]] = {'Molar Mass':a[1],'Atomic Number':a[2],'Density':a[3],'Number of Isotopes':a[4],'Isotope Data':iso_dict}  
    return element_data
#    return element_data    



        
  
