#동국대학교 정보통신공학과 2019112110 이정민
import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if len(text) == 0:
        return None
    
    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def encode_huffman_tree(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    encode_huffman_tree(root.left, current_code + "0", codes)
    encode_huffman_tree(root.right, current_code + "1", codes)

def huffman_encoding(text):
    root = build_huffman_tree(text)
    codes = {}
    encode_huffman_tree(root, "", codes)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

def huffman_decoding(encoded_text, codes):
    reverse_codes = {value: key for key, value in codes.items()}
    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text

def calculate_variance(codes):
    code_lengths = [len(code) for code in codes.values()]
    avg_length = sum(code_lengths) / len(code_lengths)
    variance = sum((length - avg_length) ** 2 for length in code_lengths) / len(code_lengths)
    return variance

if __name__ == "__main__":
    input_string = "aabcdad"
    encoded_text, codes = huffman_encoding(input_string)
    print("Huffman Code for each symbol:")
    for symbol, code in codes.items():
        print(f"Symbol: {symbol}, Code: {code}")

    print("\nEncoded text:")
    print(encoded_text)

    decoded_text = huffman_decoding(encoded_text, codes)
    print("\nDecoded text:")
    print(decoded_text)

    variance = calculate_variance(codes)
    print(f"\nVariance of the code lengths: {variance}")