# remove comments from text file

import re 

def comment_remove(line):
    line = re.sub(r'#.*$',"",line)
    return(line)

