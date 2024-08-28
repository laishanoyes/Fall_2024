"""
This script tests if a site in a FASTA file at a specified position is in Hardy-Weinberg equilibrium.

It reads a FASTA file containing DNA sequences, calculates allele and genotypic frequencies 
at a specified position, and performs a chi-squared test to determine if the observed genotypic 
frequencies match those expected under Hardy-Weinberg equilibrium.

The script handles heterozygous individuals using IUPAC codes, where each code represents a 
combination of two alleles. For example, 'M' represents 'A'/'C'.

The script outputs the following:
1. Allele frequencies for each allele.
2. Observed genotypic frequencies.
3. Expected genotypic frequencies.
4. The chi-squared value.
5. The p-value from the chi-squared test.

Usage:
    python hwe_test.py <fasta_file> <position>

Example:
    python hwe_test.py example.fasta 10

This example will check for Hardy-Weinberg equilibrium at position 10 in the sequences 
provided in the "example.fasta" file.
"""

import sys  # Import the sys module to handle command-line arguments
from scipy.stats.distributions import chi2  # Import chi2_contingency from scipy for statistical tests

# IUPAC codes for heterozygous genotypes
IUPAC_CODES = {
    'M': ('A', 'C'),  # A/C
    'R': ('A', 'G'),  # A/G
    'W': ('A', 'T'),  # A/T
    'S': ('C', 'G'),  # C/G
    'Y': ('C', 'T'),  # C/T
    'K': ('G', 'T')   # G/T
}

# Function to parse the FASTA file and extract sequences
def parse_fasta(fasta_file):
    sequences = []  # Initialize a list to store sequences
    with open(fasta_file, 'r') as file:  # Open the FASTA file for reading
        seq = ''  # Initialize an empty string to store a sequence
        for line in file:  # Iterate through each line in the file
            line = line.strip()  # Remove leading/trailing whitespace
            if line.startswith('>'):  # Check if the line is a header (starts with '>')
                if seq:  # If a sequence is already collected, add it to the list
                    sequences.append(seq)
                seq = ''  # Reset the sequence string for the next sequence
            else:
                seq += line  # Append the line to the current sequence
        if seq:  # Add the last sequence if it exists
            sequences.append(seq)
    return sequences  # Return the list of sequences


# Function to calculate allele frequencies at a specified position
def get_allele_frequencies(sequences, position):
    alleles = {}  # Initialize a dictionary to count alleles
    for seq in sequences:  # Iterate through each sequence
        allele = seq[position - 1]  # Get the allele at the specified position
        if allele in IUPAC_CODES:  # Check if the allele is a heterozygous IUPAC code
            for base in IUPAC_CODES[allele]:  # If so, count each base in the IUPAC code
                if base in alleles:
                    alleles[base] += 1
                else:
                    alleles[base] = 1
        else:
            if allele in alleles:  # Check if the allele is already in the dictionary
                alleles[allele] += 2  # Increment the count for this allele
            else:
                alleles[allele] = 2  # Initialize the count for this allele
    total_alleles = sum(alleles.values())  # Calculate the total number of alleles
    frequencies = {allele: count / total_alleles for allele, count in alleles.items()}  # Calculate the frequency for each allele

    # *************************************************************************
    # -------------------------------------------------------------------------
    # Print the observed allele frequencies here
    print("The observed allele frequencies are: " + str(frequencies))
    # -------------------------------------------------------------------------
    # *************************************************************************

    return frequencies  # Return the dictionary of allele frequencies

# Function to calculate observed genotypic frequencies
def get_genotypic_frequencies(sequences, position):
    genotypes = {}  # Initialize a dictionary to count genotypes
    for seq in sequences:  # Iterate through each sequence
        allele = seq[position - 1]  # Get the allele at the specified position
        if allele in IUPAC_CODES:  # Check if the allele is a heterozygous IUPAC code
            genotype = ''.join(sorted(IUPAC_CODES[allele]))  # Sort the alleles to create a standard genotype key
        else:
            genotype = allele + allele  # Homozygous genotype
        if genotype in genotypes:  # Check if the genotype is already in the dictionary
            genotypes[genotype] += 1  # Increment the count for this genotype
        else:
            genotypes[genotype] = 1  # Initialize the count for this genotype
    total_genotypes = sum(genotypes.values())  # Calculate the total number of genotypes
    frequencies = {genotype: count / total_genotypes for genotype, count in genotypes.items()}  # Calculate the frequency for each genotype

    # *************************************************************************
    # -------------------------------------------------------------------------
    # Print the observed genotype numbers (number of individuals) here
    print("Observed genotype numbers: " + str(genotypes))
    # -------------------------------------------------------------------------
    # *************************************************************************

    # *************************************************************************
    # -------------------------------------------------------------------------
    # Print the observed genotype frequencies here
    print("Observed genotype frequencies: " + str(frequencies))
    # -------------------------------------------------------------------------
    # *************************************************************************

    return genotypes, frequencies  # Return the dictionary of genotypes and their frequencies


# Function to calculate expected genotypic frequencies based on allele frequencies
def calculate_expected_genotypic_frequencies(allele_freqs, n):
    # Extract the present alleles and their frequencies
    # n = sample size
    alleles = list(allele_freqs.keys())

    # Initialize a dictionary to store expected genotypic frequencies
    expected_frequencies = {}
    expected_genotypes = {}
    # Iterate through each allele pair to calculate expected genotypic frequencies
    for i in range(len(alleles)):
        for j in range(i, len(alleles)):
            allele1 = alleles[i]
            allele2 = alleles[j]
            if i == j:
                # *************************************************************************
                # -------------------------------------------------------------------------
                # THERE IS A BUG HERE THAT YOU NEED TO FIX
                expected_frequencies[allele1 + allele2] = allele_freqs[allele1] * 2  # Expected frequency for the homozygous genotype (e.g., AA)
                # -------------------------------------------------------------------------
                # *************************************************************************

            else:
                # *************************************************************************
                # -------------------------------------------------------------------------
                # THERE IS A BUG HERE THAT YOU NEED TO FIX
               expected_frequencies[allele1 + allele2] = allele_freqs[allele1] * allele_freqs[allele2]  # Expected frequency for the heterozygous genotype (e.g., AC)
                # -------------------------------------------------------------------------
                # *************************************************************************

            # *************************************************************************
            # -------------------------------------------------------------------------
            # THERE IS A BUG HERE THAT YOU NEED TO FIX
            expected_genotypes[allele1 + allele2] = expected_frequencies[allele1 + allele2] * (n / 2)
            # -------------------------------------------------------------------------
            # *************************************************************************

    # *************************************************************************
    # -------------------------------------------------------------------------
    # Print the observed genotype numbers (number of individuals) here
    print("Expected genotype numbers: ")
    # -------------------------------------------------------------------------
    # *************************************************************************

    # *************************************************************************
    # -------------------------------------------------------------------------
    # Print the observed genotype frequencies here
    print("Expected genotype frequencies: ")
    # -------------------------------------------------------------------------
    # *************************************************************************

    return expected_genotypes, expected_frequencies  # Return the dictionary of expected genotypic frequencies

# -------------------------------------------------------------------------

# Function to perform chi-square test to compare observed and expected frequencies
def chi_square_test(observed, expected):
    observed_values = list(observed.values())  # Convert observed genotype counts to a list
    print(observed_values)
    expected_values = list(expected.values())  # Convert expected genotype frequencies to a list
    print(expected_values)

    total = sum(observed_values)  # Calculate the total number of observed genotypes
    
    # Calculate chi-squared statistic
    chi2_stat = 0
    for i in range(0,len(observed_values)):
        # *************************************************************************
        # -------------------------------------------------------------------------
        # THERE IS A BUG HERE THAT YOU NEED TO FIX
        chi2_stat += (((observed_values[i] + expected_values[i]) ** 2) / expected_values[i])
        # -------------------------------------------------------------------------
        # *************************************************************************

    # *************************************************************************
    # -------------------------------------------------------------------------
    # Print the chi-squared value
    print("text for printing chi-squared value")
    # -------------------------------------------------------------------------
    # *************************************************************************


    return chi2_stat  # Return the chi-squared statistic

# -------------------------------------------------------------------------

# Main function to tie everything together
# *** YOU NEED TO PRINT THE P-VALUE *** #
def main(fasta_file, position):
    sequences = parse_fasta(fasta_file)  # Parse the FASTA file to get sequences
    n_seq = len(sequences)
    allele_frequencies = get_allele_frequencies(sequences, position)  # Get allele frequencies at the specified position
    observed_genotypes, observed_genotype_frequencies = get_genotypic_frequencies(sequences, position)  # Get observed genotypic frequencies
    expected_genotypes, expected_genotype_frequencies = calculate_expected_genotypic_frequencies(allele_frequencies, n_seq)  # Calculate expected genotypic frequencies

    chi2_stat = chi_square_test(observed_genotypes, expected_genotypes)  # Calculate the chi-squared value

    # Calculate p-value from chi-squared test (with 1 degree of freedom for HWE test)
    p_value = chi2.sf(chi2_stat, 1)


    # *************************************************************************
    # -------------------------------------------------------------------------
    # Print the p-value value
    print("text for printing p-value")
    # -------------------------------------------------------------------------
    # *************************************************************************


    # *************************************************************************
    # -------------------------------------------------------------------------
    # Print the interpretation of the p-value
    if p_value > 0.05:
        print("insert interpretation of p-value <0.05 here")
    else:
        print("insert interpretation of p-value >0.05 here")
    # -------------------------------------------------------------------------
    # *************************************************************************

# Script entry point
if __name__ == "__main__":
    if len(sys.argv) != 3:  # Check if the correct number of arguments is provided
        print("Usage: python hwe_test.py <fasta_file> <position>")  # Print usage instructions
    else:
        fasta_file = sys.argv[1]  # Get the FASTA file from the command-line arguments
        position = int(sys.argv[2])  # Get the position as an integer from the command-line arguments
        main(fasta_file, position)  # Call the main function with the provided arguments
