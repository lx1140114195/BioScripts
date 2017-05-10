from Bio import Entrez as E
from Bio import SeqIO
E.email = "ns196414@ohio.edu"   
import sys
import re
from openpyxl import *
from openpyxl.styles import Font, Border, Side

accre = re.compile('Accession',re.IGNORECASE)
wb = load_workbook(str(sys.argv[1]))
wb.guess_types = True
ws = wb.worksheets[0]
seqList = []
for index,row in enumerate(ws.rows,start=1):
    if index != 1:
        acces = row[8].value
        match = accre.search(str(acces))
        if acces != None and not match:
            seqList.append(acces.replace('\xa0',''))
            
#Write them all to a file
h = E.efetch(db="nucleotide", id=seqList, rettype="gb", retmode="text")
r = SeqIO.parse(h,"genbank")
SeqIO.write(r,"sequences.gb","genbank")
