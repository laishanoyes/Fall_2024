import sys
from Bio import SeqIO

"""
This script calculates Fst from a site in a multiple sequence fasta alignment
Individuals are assigned to either group 1 or group 2
Each individual name is followed by "-1" or "-2" to represent group ID
The user specifies which site is to be examined

--------------------

Example usage:
python calculate-Fst.py subpop_alignment_abbrev.fasta 25

--------------------

Assignment:

1. Add your code to the areas indicated below.
2. Print the resulting Fst value
3. Provide an interpretation for the Fst value
"""

# Define the IUPAC codes for heterozygous individuals
IUPAC_CODES = {
    'R': ('A', 'G'),
    'Y': ('C', 'T'),
    'S': ('C', 'G'),
    'W': ('A', 'T'),
    'K': ('G', 'T'),
    'M': ('A', 'C')
}

def get_allele_frequencies_diploid(group_sequences, position):
    """
    Calculate the allele frequencies at a specific position for a group of diploid sequences.
    This function takes into account both homozygous and heterozygous genotypes, following the IUPAC naming convention.

    Parameters:
    group_sequences (list of str): List of sequences (DNA strings) belonging to a group.
    position (int): Position in the sequence to extract the alleles (0-based index).

    Returns:
    dict: Allele frequencies at the specified position.
    """
    allele_counts = {}
    total_alleles = 0  # Total number of alleles (since each individual contributes 2 alleles)

    # Loop through the diploid sequences
    for seq in group_sequences:
        allele = seq[position]  # Allele at the specified position

        # Check if the allele is heterozygous using IUPAC codes
        if allele in IUPAC_CODES:
            # Split the heterozygous genotype into two alleles
            allele1, allele2 = IUPAC_CODES[allele]
            allele_counts[allele1] = allele_counts.get(allele1, 0) + 1
            allele_counts[allele2] = allele_counts.get(allele2, 0) + 1
            total_alleles += 2
        else:
            # Treat as homozygous (e.g., "C" -> "CC")
            allele_counts[allele] = allele_counts.get(allele, 0) + 2
            total_alleles += 2

    if total_alleles == 0:
        return {}

    # Convert allele counts to frequencies
    allele_frequencies = {allele: count / total_alleles for allele, count in allele_counts.items()}

    return allele_frequencies

def calculate_Fst(fasta_file, position):
    """
    Calculate Fst from a single, specified position in a sequence alignment for diploid individuals.
    
    Fst is calculated using the equation Fst = (HT - HS) / HT.

    Parameters:
    fasta_file (str): Path to the FASTA file containing sequence alignments.
    position (int): The nucleotide position (0-based) in the alignment for Fst calculation.

    Returns:
    float: The Fst value at the specified position.
    """
    
    # Initialize lists to store sequences for each group
    group1_seqs = []  # Sequences ending in '-1'
    group2_seqs = []  # Sequences ending in '-2'
    
    # Parse the FASTA file and separate sequences into groups
    for record in SeqIO.parse(fasta_file, "fasta"):
        identifier = record.id  # The identifier (name) of the sequence
        sequence = str(record.seq)  # The DNA sequence
        if identifier.endswith("-1"):  # Group 1 identifier
            group1_seqs.append(sequence)
        elif identifier.endswith("-2"):  # Group 2 identifier
            group2_seqs.append(sequence)
    
    # Ensure that both groups have at least one sequence
    if not group1_seqs or not group2_seqs:
        raise ValueError("Both groups (-1 and -2) must have at least one individual.")
    
    # Calculate allele frequencies for both groups at the given position (as diploid with heterozygotes)
    freqs1 = get_allele_frequencies_diploid(group1_seqs, position)  # Group 1 allele frequencies
    print(freqs1)
    freqs2 = get_allele_frequencies_diploid(group2_seqs, position)  # Group 2 allele frequencies
    print(freqs2)

    # Make sure both groups have the same set of alleles (add missing alleles with frequency 0)
    all_alleles = set(freqs1.keys()).union(set(freqs2.keys()))
    for allele in all_alleles:
        freqs1.setdefault(allele, 0)
        freqs2.setdefault(allele, 0)

    # We assume a biallelic case: calculate frequency of the first allele in both groups
    p1 = freqs1[list(all_alleles)[0]]
    p2 = freqs2[list(all_alleles)[0]]
    
    # Calculate HS (within-group heterozygosity)
    ### ************************** ###
    ### *** ADD YOUR CODE HERE *** ###
    HS = ((2 * p1 * (1-p1)) + (2 * p2 * (1-p2))) // 2
    ### ************************** ###
    ### ************************** ###
   
    # Calculate HT (total population heterozygosity)
    ### ************************** ###
    ### *** ADD YOUR CODE HERE *** ###
    HT = (((2 * (p1 + p2)
    ### ************************** ###
    ### ************************** ###

    # Calculate Fst: Fst = (HT - HS) / HT
    ### ************************** ###
    ### *** ADD YOUR CODE HERE *** ###
    Fst = 0  # Avoid division by zero
    ### ************************** ###
    ### ************************** ###

    return Fst

if __name__ == "__main__":
    fasta_file = sys.argv[1]  # Replace with the path to your FASTA file
    position = int(sys.argv[2]) - 1  # Replace with the desired nucleotide position (0-based index)
    fst_value = calculate_Fst(fasta_file, position)  # Calculate Fst
    # Print Fst value
    ### ************************** ###
    ### *** ADD YOUR CODE HERE *** ###
    print("Print Fst value here")
    ### ************************** ###
    ### ************************** ###

    # Print Fst interpretation
    ### ************************** ###
    ### *** ADD YOUR CODE HERE *** ###
    print("Print interpretation here")
    ### ************************** ###
    ### ************************** ###
