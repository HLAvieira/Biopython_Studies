from Bio.Blast import NCBIWWW
result_handle2 = NCBIWWW.qblast('blastn', 'nt', 'MT232872')
with open('blas-test-result.xml', 'w') as out_handle:
    out_handle.write(result_handle2.read())
result_handle2.close()

