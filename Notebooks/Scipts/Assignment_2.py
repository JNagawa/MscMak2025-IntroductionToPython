#!/jnagawa/bin/env python3
"""
FASTA Random DNA Generator
Author: Jovita Nagawa
Date: 2025-11-05
#####....Description.....###:
    This script generates random DNA sequences in FASTA format.
    Usage:
        python sequence_generator.py <num_sequences> <seq_length> <output_file>
"""

import sys
import random

def generate_dna_sequence(length):
    """Generate a random DNA sequence of given length."""
    nucleotides = ['A', 'T', 'C', 'G']
    return ''.join(random.choices(nucleotides, k=length))

def write_fasta(sequences, output_file):
    """Write sequences to a file in FASTA format with 80 nucleotides per line."""
    with open(output_file, 'w') as f:
        for i, seq in enumerate(sequences, start=1):
            f.write(f">Sequence_{i}\n")
            # Break sequence into lines of max 80 chars
            for j in range(0, len(seq), 80):
                f.write(seq[j:j+80] + '\n')
def main():
    """Main function to handle command-line arguments and generate sequences."""
    if len(sys.argv) != 4:
        print("Usage: python fasta_generator.py <num_sequences> <seq_length> <output_file>")
        sys.exit(1)

    try:
        num_sequences = int(sys.argv[1])
        seq_length = int(sys.argv[2])
        output_file = sys.argv[3]
    except ValueError:
        print("Error: num_sequences and seq_length must be integers.")
        sys.exit(1)

    # Generate sequences
    sequences = [generate_dna_sequence(seq_length) for _ in range(num_sequences)]

    # Write to FASTA file
    write_fasta(sequences, output_file)
    print(f"{num_sequences} sequences of length {seq_length} written to {output_file}.")

if __name__ == "__main__":
    main()
