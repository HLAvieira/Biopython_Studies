import csv
with open("C:\Biopyhton_files\sc_wt_chr3_genes.csv.txt", newline= '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ' ', quotechar='|')
    sc_wt_chr_iii_list = [x[0:-1] for x in list(csvfile) if len(x) > 0]
for i in sc_wt_chr_iii_list:
    print(i)

print(sc_wt_chr_iii_list)
print('Há {} elementos nessa lista'.format(len(sc_wt_chr_iii_list)))

