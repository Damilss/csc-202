from huffman import HuffmanLeaf, build_huffman_tree

from typing import TextIO


def parse_header(header:str)-> list[int]:
    """Takes the first line of the file as an argument and will return
    a list of ints that represent the frequencies. The list of frequencies should be in the same format that function 
    count_frequencies returns
    
    (a list with 256 entries, indexed by the ASCII value of the characters)"""
    freqs = [0] * 256
    
    header = header.strip()
    if header == "":
        return freqs

    parts = header.split()
    
    for i in range(0, len(parts), 2):
        ascii_val = int(parts[i])
        freq = int(parts[i + 1])
        freqs[ascii_val] = freq

    return freqs

def huffman_decoding(input_file: TextIO, output_file:TextIO) -> TextIO: 
    """Takes two open files, and stores the resulting decoded data in an output file"""
    header_line = input_file.readline().rstrip("\n")
    freqs = parse_header(header_line)

    total_chars = sum(freqs)
    
    if total_chars == 0:
        return output_file

    tree = build_huffman_tree(freqs)

    if isinstance(tree, HuffmanLeaf):
        output_file.write(chr(tree.char) * total_chars)
        return output_file

    node = tree
    written = 0 
    bits = input_file.read()

    for bit in bits:
        if written >= total_chars:
            break

        if bit == "0":
            node = node.left
        elif bit == "1":
            node = node.right

        if isinstance(node, HuffmanLeaf):
            output_file.write(chr(node.char))
            written +=1
            node = tree

    return output_file
