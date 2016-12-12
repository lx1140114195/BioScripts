# Convert to tbl format from mfannot to gff version 3
# https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md
# Run me: python3 tblToGff.py < <fileName> > <outfile>
from sys import stdin
import re 

# The format of the file that we are trying to convert to:
# ##gff-version 3
# Balb1 .  gene 1286 3 .  +  . ID=gene1;Name=sufB


# First we print the version number header
print('##gff-version 3')

# Then we use sys.stdin to read in from standard input and remove any endline or tab sometimes replacing them with spaces
# It is assigned to the variable better for some reason and is string
better = stdin.read().replace('\n',' ').replace('\r\n','').replace('\r','').replace('\t', ' ')

# findline is a regular expression that matches the two rows in the tbl format:
findline = re.compile('\d+\s\d+\sgene\s+gene\s\w+[\(\w\)]*',re.DOTALL)

# The first row has the start and end location
# The second row has the gene name


# Some examples from our input file
# 1286	3	gene
#         		gene	sufB

# 20798	20726	gene
#			gene	trnR(ccg)

# Follow the link to learn more about regular expression in python3
# https://docs.python.org/3/howto/regex.html


# This returns a list of all regular expressions(re) that findall matches in better.  Better has spaces instead of newlines and tabs (\t)
# These are assigned to the list variable matches
matches = findline.findall(better)

# Now for each  match in the list matches  
num = 1 # Count for the gene identifer to satisfy the gff format
for match in matches:
    #trimmed the matched string down to only the start end and genename
    match = match.replace('gene','') # replaces gene with ''
    match = re.sub('\s\s+',' ',match) # substitutes 2 whitespace characters followed by any number of whitespaces with ' '

    # splits on spaces and makes a list which is then assigned to start end and gname.
    start,end,gname=match.split() #might have to add one to start and end since tbl might be 0 indexed and gff is 1 based
    

    #Checks to see if the start is greater than end and if so will output a - instead of + in column 7
    # I still haven't tested this it might not work the documentation for gff is kind of confusing 
    isrev = '+'
    if int(start) > int(end):
        isrev = '-'
        

    #prints the gff
    print('Balb1 .  gene ', start, ' ' , end,' .  ', isrev,'  . ID=gene',
          num,';Name=',gname,sep='')
    num+=1
    


