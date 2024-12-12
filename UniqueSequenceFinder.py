import sys
from typing import Set, Dict, List, Tuple


class RNAParse:
    """
    Analyzes RNA sequences to find unique subsequences.
    
    This class provides functionality to analyze RNA sequences, find unique
    regions, and display them in a scaffolded format.
    """
    
    def __init__(self, sequence: str, header: str):
        """
        Initialize the RNA parser with a sequence and its header.
        
        Args:
            sequence: The RNA sequence to analyze
            header: The header/identifier for the sequence
        """
        self.sequence = sequence
        self.header = header

    def SequenceString(self, string: str) -> Set[str]:
        """
        Generate all possible subsequences from a given string.
        
        Args:
            string: Input string to generate subsequences from
            
        Returns:
            Set of all possible subsequences
        """
        seqset = set()
        
        # Generate all possible subsequences by varying length and position
        for length in range(len(string), 0, -1):
            for start in range(len(string) - length + 1):
                seqstr = string[start:start + length]
                seqset.add(seqstr)
                
        return seqset

    def UniqueFinder(self, sequences_dict: Dict[str, Set[str]]) -> Set[str]:
        """
        Find sequences unique to the current header's set.
        
        Args:
            sequences_dict: Dictionary mapping headers to their sequence sets
            
        Returns:
            Set of sequences unique to the current header
        """
        # Get the set for current header
        target_set = sequences_dict[self.header]
        
        # Create union of all other sets
        sequences_dict.pop(self.header)
        other_sequences = set().union(*sequences_dict.values())
        
        # Restore the dictionary
        sequences_dict[self.header] = target_set
        
        # Return sequences unique to target set
        return target_set.difference(other_sequences)

    def SetReducer(self, unique_set: Set[str]) -> Set[str]:
        """
        Reduce a set of strings to its minimal unique subsequences.
        
        Args:
            unique_set: Set of unique sequences to reduce
            
        Returns:
            Set of minimal unique subsequences
        """
        lowest_set = set()
        
        for seq in unique_set:
            # If sequence has only one intersection with the unique set,
            # it's a minimal unique subsequence
            if len(unique_set.intersection(self.SequenceString(seq))) == 1:
                lowest_set.add(seq)
                
        return lowest_set

    def seqPrinter(self, unique_set: Set[str]):
        """
        Print sequences in a scaffolded display format.
        
        Args:
            unique_set: Set of sequences to display
        """
        # Write header and sequence
        sys.stdout.write(f"{self.header}\n{self.sequence}\n")
        
        # Create position-based dictionary
        position_dict = {
            self.sequence.find(x): x for x in unique_set
        }
        
        # Get sorted positions
        positions = sorted(position_dict.keys())
        
        # Print scaffolded display
        for pos in positions:
            seq = position_dict[pos]
            dots_before = "." * pos
            dots_after = "." * (len(self.sequence) - pos - len(seq))
            sys.stdout.write(f"{dots_before}{seq}{dots_after}\n")


class FastAreader:
    """Handles reading of FASTA format files."""
    
    def __init__(self, fname: str = ''):
        """
        Initialize with a filename.
        
        Args:
            fname: Name of the FASTA file to read (empty for stdin)
        """
        self.fname = fname

    def doOpen(self):
        """Open the file or return stdin if no filename provided."""
        return sys.stdin if not self.fname else open(self.fname)

    def readFasta(self) -> Tuple[str, str]:
        """
        Read sequences from a FASTA file.
        
        Yields:
            Tuple of (header, sequence) for each FASTA entry
        """
        with self.doOpen() as fileH:
            header = ''
            sequence = ''
            
            # Find first FASTA header
            line = fileH.readline()
            while not line.startswith('>'):
                if not line:  # EOF
                    return header, sequence
                line = fileH.readline()
            header = line[1:].rstrip()
            
            # Read sequences
            for line in fileH:
                if line.startswith('>'):
                    yield header, sequence
                    header = line[1:].rstrip()
                    sequence = ''
                else:
                    sequence += ''.join(line.rstrip().split()).upper()
                    
            yield header, sequence


def main(inCL=None):
    """
    Main function to process RNA sequences and find unique regions.
    
    This function reads sequences, finds unique regions, and displays them
    in a scaffolded format.
    """
    reader = FastAreader("")
    sequences_dict = {}
    headers = []
    sequences = {}

    # Read and process all sequences
    for header, sequence in reader.readFasta():
        # Clean up header and sequence
        header = header.replace(" ", "")
        sequence = sequence.translate(str.maketrans("", "", "-_."))
        
        headers.append(header)
        sequences[header] = sequence
        
        parser = RNAParse(sequence, header)
        sequences_dict[header] = parser.SequenceString(sequence)

    # Process each sequence in alphabetical order
    for header in sorted(headers):
        parser = RNAParse(sequences[header], header)
        unique_seqs = parser.UniqueFinder(sequences_dict)
        minimal_seqs = parser.SetReducer(unique_seqs)
        parser.seqPrinter(minimal_seqs)


if __name__ == "__main__":
    main()