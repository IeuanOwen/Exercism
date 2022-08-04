def to_rna(dna_strand):
    alts = "".maketrans("GCTA", "CGAU")
    dna_strand = dna_strand.translate(alts) if dna_strand != "" else dna_strand
    return dna_strand
