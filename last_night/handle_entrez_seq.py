# Handle entrez sequences
from Bio import Entrez
from Bio import SeqIO
import os
Entrez.email = "hugovieiraunb@gmail.com"
filename = 'KC880027.fasta'
#creating a file named 'KC880027.fasta'
'''if not os.path.isfile(filename):
    net_handle = Entrez.efetch(db='nucleotide', rettype='fasta', retmode='text', id='KC880027')
    out_handle = open(filename, 'w')
    out_handle.write(net_handle.read())
    out_handle.close()
    net_handle.close()
    print('saved')
print('Parsing...')
record = SeqIO.read(filename, 'fasta')
print(record.seq)'''

'''file2 = 'KC880027_extract.fasta'
if not os.path.isfile(file2):'''

# parsing and slicing gb format
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="xml", id="KC880027")
record = Entrez.read(handle)
handle.close()
print(record[0]['GBSeq_sequence'][1:11])
'''print(record.description)
print(record.name)
a = 305
b = 325
print(record.seq[a:b+1]) #TACCCTAATAACTTCGTATAG'''