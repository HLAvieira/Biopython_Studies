from Bio import Entrez
Entrez.email = 'hugovieiraunb@gmail.com'
'''handle = Entrez.einfo()
record = Entrez.read(handle) #now recor is a dictionary with one key 'DbList'
print(record.keys())
print(record['DbList']) # The values stored in this key is the list of database names shown in the XML'''
'''result = handle.read()
handle.close()
print(result)'''
handle = Entrez.einfo(db='pubmed')
record = Entrez.read(handle)
print(record)
print(record['DbInfo']['Description'])
print(record['DbInfo']['LastUpdate'])