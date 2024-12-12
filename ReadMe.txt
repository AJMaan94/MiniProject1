UniqueSeq: A Unique Subsequence Finder for DNA/RNA Analysis
Version 1.0
Overview
UniqueSeq is a Python-based tool designed to identify unique subsequences within DNA or RNA sequences. It analyzes multiple sequences simultaneously and identifies regions that are unique to each sequence, making it valuable for primer design, sequence signature identification, and comparative genomic analysis.
Features

Reads FASTA format sequences
Identifies all possible subsequences
Finds unique regions specific to each sequence
Reduces findings to minimal unique subsequences
Displays results in an easy-to-read scaffolded format
Supports both file input and standard input
Case-insensitive sequence processing
Automatic handling of common sequence formatting issues

Requirements

Python 3.6 or higher
Standard Python libraries (no additional dependencies required)
Input sequences in FASTA format

Installation

Download the script files:
Copyuniqueseq.py

Make the script executable (Unix/Linux):
bashCopychmod +x uniqueseq.py


Usage
Basic Usage
bashCopypython uniqueseq.py < input.fasta
or
bashCopycat input.fasta | python uniqueseq.py
Input Format
The tool accepts FASTA format files. Example:
Copy>Sequence1
ATGCTAGCTAGCT
>Sequence2
ATGCTAGCTAGGA
Output Format
The output is displayed in a scaffolded format:
Copy>Sequence1
ATGCTAGCTAGCT
...GCT........
.....TAG......

>Sequence2
ATGCTAGCTAGGA
.........AGGA.

First line: Sequence header
Second line: Complete sequence
Following lines: Unique subsequences with position indicated by dots

Example Usage

Analysis of multiple sequences:

bashCopy# Create input file
echo ">Seq1
ATGCTAGCT
>Seq2
ATGCTAGGA" > input.fasta

# Run analysis
python uniqueseq.py < input.fasta

Direct input:

bashCopypython uniqueseq.py
>Seq1
ATGCTAGCT
>Seq2
ATGCTAGGA
[Ctrl+D to end input]
Technical Details
Algorithm Overview

Sequence Processing:

Reads FASTA format input
Removes spaces and special characters
Converts sequences to uppercase


Subsequence Generation:

Generates all possible subsequences
Creates sets for efficient comparison


Unique Region Identification:

Compares subsequence sets between sequences
Identifies regions unique to each sequence


Minimal Subsequence Reduction:

Reduces unique regions to minimal length
Ensures non-redundancy



Performance Considerations

Memory usage scales with sequence length
Processing time increases with sequence length and count
Efficient for typical gene-length sequences

Common Issues and Solutions
Input Issues

Problem: Sequences contain special characters
Solution: Tool automatically removes -, _, ., and spaces
Problem: Mixed case in sequences
Solution: Tool automatically converts all sequences to uppercase

Output Issues

Problem: Output appears misaligned
Solution: Ensure terminal width is sufficient for sequence length

Limitations

Memory intensive for very long sequences
Processing time increases significantly with sequence length
Limited to ASCII characters in sequences

Contributing
Contributions are welcome! Please feel free to submit issues and pull requests.
License
This tool is available under the MIT License.
Author
Amarjot Maan
Contact
For issues, suggestions, or questions, please create an issue in the repository.
Version History

1.0: Initial release

Basic subsequence finding functionality
FASTA format support
Scaffolded output display