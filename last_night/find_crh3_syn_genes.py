from Bio import SeqIO
list_of_chriii_syn_genes = []
for seq_record in SeqIO.parse("C:\Biopyhton_files\chriii_syn.fasta", "fasta"):
    if ((seq_record.description[22]) != ' ') and ((seq_record.description[23] != ' ')):
        if (seq_record.description[28+7] != ']'):
            list_of_chriii_syn_genes.append(seq_record.description[28:28 + 9])
        else:
            list_of_chriii_syn_genes.append(seq_record.description[28:28+7])
    elif ((seq_record.description[23]) != (' ')):
        if (seq_record.description[29+7] != ']'):
            list_of_chriii_syn_genes.append(seq_record.description[29:29 + 9])
        else:
            list_of_chriii_syn_genes.append(seq_record.description[29:29+7])
    else:
        if (seq_record.description[30+7] != ']'):
            list_of_chriii_syn_genes.append(seq_record.description[30:30 + 9])
        else:
            list_of_chriii_syn_genes.append(seq_record.description[30:30+7])
print(list_of_chriii_syn_genes)
print(len(list_of_chriii_syn_genes))
print(list_of_chriii_syn_genes[2])
for item in list_of_chriii_syn_genes:
    print(item)

