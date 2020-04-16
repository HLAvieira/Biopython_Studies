from Bio import SearchIO
blastq_result = SearchIO.read(r'C:\Users\Hugo\Documents\Meus_projetos\Studies\last_night\blast-test-result.xml', 'blast-xml')
print(blastq_result)
blat_query_result = SearchIO.read(r'C:\Users\Hugo\Documents\Meus_projetos\clonados\biopython\Doc\examples\my_blat.psl', 'blat-psl')
#print(blat_query_result)
print(f'blast program is {blastq_result.program}, it`s version is {blastq_result.version}')
print(f'blat program is {blat_query_result.program}, blat version is {blat_query_result.version}')
#for hit in blastq_result:
#    print(hit)
#print(blastq_result['gi|262205445|ref|NR_030221.1|'])
print(blastq_result.hits) # list of all hits
print(blastq_result.hit_keys) #list of all hit IDs