# remove comments from text file

import re 
file = open('commentfile.std')
def comment_remove(line):
    line = re.sub(r'#.*$',"",line)
    return(line)

for line in file
    line = comment_remove(line)
print(line)
