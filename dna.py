import csv
import sys


def main():

    # Check for command-line usage
    if (len(sys.argv) < 2):
        print("Usage: python dna.py data.csv sequence.txt")
        return 1

    # Read database file into a variable
    dna_sequences = []
    dna_dict = {}
    dna_text = open(sys.argv[1], "r")

    with open(sys.argv[1], newline='') as csvfile:
        dna_database = csv.DictReader(csvfile, delimiter=',')
        dna_sequences = dna_database.fieldnames
        for row in dna_database:
            dna_dict[row[dna_sequences[0]]] = row
    # Read DNA sequence file into a variable
    text_file = open(sys.argv[2], "r")
    dna_text = text_file.readline()
    dna_sequences.pop(0)

    # Get longest matches from file, put into a dict
    longest_match_dna = {}
    for subsequence in dna_sequences:
        longest_match_dna[subsequence] = (longest_match(dna_text, subsequence))

    # Find longest match of each STR in DNA sequence
    # Check database for matching profiles
    print(return_matching_dna(longest_match_dna, dna_dict, dna_sequences))
    return 0


def return_matching_dna(read_sequence, character_dict, dna_sequences):
    """Returns the character that matches the read sequence"""

    # Parse through each character from database
    for name in character_dict:
        # Compare DNA in character with dna in sequence
        match = True
        for sequence in dna_sequences:
            # Pull from dictionaries the sequence values from the person and the data file
            read_sequence_comparator = read_sequence[sequence]
            character_comparator = character_dict[name][sequence]

            # If we do not have a match, we break the loop; all dna must match therefore speeds up efficiency
            if not (int(read_sequence_comparator) == int(character_comparator)):
                match = False
                break

        # If we parsed through loop and all matched, then we know this person matches the dna
        if match:
            return name

    return "No match"


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
