from Bio import Entrez
Entrez.email = 'hugovieiraunb@gmail.com'
'''handle = Entrez.esearch(db='pubmed', term='biopython')
record = Entrez.read(handle)
print(record)
print(record['IdList'])
for i in record['IdList']:
    print(i)'''
handle = Entrez.esearch(db='nucleotide', term='Cryptococcus[Orgn] AND ade2[Gene]', idtype='acc')
record = Entrez.read(handle)
print(record)
'''handle = Entrez.esearch(db='genome', term='txid4930[Organism:exp]')
record = Entrez.read(handle)
print(record)'''
# retrieving document summaries from a list of primary IDs
c = 0
# loop to print summaries for all Id in IdList above
for i in record['IdList']:
    handle_summ = Entrez.esummary(db='nucleotide', id=record['IdList'][c])
    record_summ = Entrez.read(handle_summ)
    print(record_summ[0]['Title']) # print only the summary title
    c += 1
