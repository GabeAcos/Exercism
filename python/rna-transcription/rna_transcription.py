def to_rna(dna_strand):
    the_dict = {'G': 'C', 'T': 'A', 'C': 'G', 'A': 'U'}
    rna_strand = ""
    for character in dna_strand:
        if character in the_dict:
            rna_strand += the_dict[character]

    return rna_strand
