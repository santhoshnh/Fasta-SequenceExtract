import argparse
from Bio import SeqIO

def extract_sequences(input_fasta, output_fasta, id_file):
    # Read sequence IDs from the text file
    with open(id_file, 'r') as id_handle:
        sequence_ids = [line.strip() for line in id_handle]

    sequences = []

    with open(input_fasta, 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            header_id = record.id.split()[0]  # Extract the ID from the header

            # Check if any part of the ID is in the header
            if any(seq_id in header_id for seq_id in sequence_ids):
                sequences.append(record)

    with open(output_fasta, 'w') as output:
        SeqIO.write(sequences, output, 'fasta')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract sequences based on partial IDs from a FASTA file.')
    parser.add_argument('input_fasta', help='Input FASTA file path')
    parser.add_argument('output_fasta', help='Output FASTA file path')
    parser.add_argument('id_file', help='File containing partial sequence IDs, one per line')

    args = parser.parse_args()

    # Call the function to extract sequences
    extract_sequences(args.input_fasta, args.output_fasta, args.id_file)

    print("Extraction complete. Check the output file:", args.output_fasta)

