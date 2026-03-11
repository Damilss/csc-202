from dataclasses import dataclass

from typing import TextIO
from heapq import heappush, heappop

type HuffmanTree = HuffmanLeaf | HuffmanNode


@dataclass(frozen=True)
class HuffmanLeaf:
    char: int
    frequency: int

    def __lt__(self, other: HuffmanTree) -> bool:
        """Return True if and only if self < other."""
        if self.frequency == other.frequency: 
            return self.char < other.char 
        
        return self.frequency < other.frequency


@dataclass(frozen=True)
class HuffmanNode:
    char: int
    frequency: int
    left: HuffmanTree
    right: HuffmanTree

    def __lt__(self, other: HuffmanTree) -> bool:
        """Return True if and only if self < other."""
        if self.frequency == other.frequency: 
            return self.char < other.char 
        
        return self.frequency < other.frequency 


def count_frequencies(file: TextIO) -> list[int]:
    """Read the given file and counts the frequency of each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the frequency with which that character occured.
    """
    char_frequency = [0] * 256
    while True: 
        char = file.read(1) 

        if char == '':
            break

        char_frequency[ord(char)] += 1 
    
    return char_frequency

    


def build_huffman_tree(frequencies: list[int]) -> HuffmanTree | None:
    """Create a Huffman tree of the characters with non-zero frequency.

    If no character has a non-zero frequency, returns None.
    """
    none_flag = True
    queue = []
     
    
    for freq_idx in frequencies:
        if freq_idx != 0:
            none_flag = False
            break 

    if none_flag: 
        return None
    
    for char, frequency in enumerate(frequencies):
        if frequency > 0:
            heappush(queue, HuffmanLeaf(char, frequency))
    
    while len(queue) > 1: 
        tree1 = heappop(queue)
        tree2 = heappop(queue)
        
        if tree1 < tree2: 
            left = tree1
            right = tree2 

        new_freq = left.frequency + right.frequency
        new_char = min(left.char, right.char)

        new_node = HuffmanNode(new_char, new_freq, left, right)
        heappush(queue, new_node)

    return queue[0]




def create_codes(tree: HuffmanTree | None) -> list[str]:
    """Traverse the tree creating the Huffman code for each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the Huffman code for that character.
    """
    codes = [""] * 256
    if tree is None:
        return codes

    if isinstance(tree, HuffmanLeaf):
        codes[tree.char] = "0"
        return codes

    def traverse(node: HuffmanTree, current: str) -> None:
        if isinstance(node, HuffmanLeaf):
            codes[node.char] = current
            return
        
        traverse(node.left, current + "0")
        traverse(node.right, current + "1")

    traverse(tree, "")
    return codes
    
    


def create_header(frequencies: list[int]) -> str:
    """Return the header for the compressed Huffman data.

    For example, given the file "aaabbbbcc", this would return:
    "97 3 98 4 99 2"
    """
    pieces = [] 
    for char, frequency in enumerate(frequencies):
        if frequency > 0: 
            pieces.append(str(char))
            pieces.append(str(frequency))

    return " ".join(pieces)




def huffman_encode(in_file: TextIO, out_file: TextIO) -> None:
    """Encode the data in the input file.

    This will write to the output file and won't return anything.
    """
    frequencies = count_frequencies(in_file)
    tree = build_huffman_tree(frequencies)
    codes = create_codes(tree)
    header = create_header(frequencies)

    out_file.write(header)
    out_file.write("\n")
    
    in_file.seek(0)
    while True:
        ch = in_file.read(1)
        if ch == "":
            break
        out_file.write(codes[ord(ch)])


