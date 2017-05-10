# Subclass Order Taxa Size(bp) GCContent(%) CDSa tRNA rRNA Accession Reference Citation	Website
# I'm going to try to respect ncbi and use their interface but I might need to scrape for some things.
import os
import re
from openpyxl import *
from openpyxl.styles import Font, Border, Side
accre = re.compile('Accession',re.IGNORECASE)
# wb = load_workbook(str(sys.argv[1]))
# wb.guess_types = True
# ws = wb.worksheets[0]
from Bio import Entrez as E
from Bio import SeqIO
E.email = "ns196414@ohio.edu"     # Always tell NCBI who you are
# handle = Entrez.efetch(db="nucleotide", id="NC_020795", rettype="gb", retmode="text")
# print(handle.read())

handle = E.esearch(db="genome",term="Chondrus crispus[orgn]")
record = E.read(handle)
print(record.keys())
import time


# from selenium import webdriver

# driver = webdriver.Chrome()
# url = "https://www.ncbi.nlm.nih.gov/nuccore/"
# driver.get()

h = E.efetch(db="nucleotide", id=["KC894740","KX284715"], rettype="gb", retmode="text")

r = SeqIO.parse(h,"genbank")
h.close()
SeqIO.write(r,"hi.gb","genbank")

rec = SeqIO.parse("hi.gb","genbank")

fcount = {}
for f in r.features:
    fcount[f.type] = 0 

for f in r.features:
    fcount[f.type] +=1 

dir(r.annotations['references'][0])



# This is if I would want to download all of some class
# handle=E.egquery(term="Florideophyceae AND complete genome")
# record = E.read(handle)
# handle.close()
# for row in record["eGQueryResult"]:
#     if row["DbName"] =="nuccore":
#         print(row['Count'])
# handle = E.esearch(db="nucleotide",term="Florideophyceae AND complete genome")
# record = E.read(handle)

