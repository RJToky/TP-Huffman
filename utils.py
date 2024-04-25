from huffman import Source, Symbole
import pickle

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
def write_source_code(file_path, S):
    with open(file_path, 'wb') as f:
        pickle.dump(S, f)

def read_source_code(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def write_bytes(file_path, binary):
    with open(file_path, 'wb') as f:
        f.write(int(binary, 2).to_bytes((len(binary) + 7) // 8, byteorder='big'))

def read_bytes(file_path):
    with open(file_path, 'rb') as f:
        return bin(int.from_bytes(f.read(), byteorder='big'))[2:]

def format_8(binary):
    write_file('nombre.txt', str(8 - len(binary) % 8))
    return binary + ('0' * (8 - len(binary) % 8))

def calculate_proba(text):
    probas = {}
    for char in text:
        if char in probas:
            probas[char] += 1
        else:
            probas[char] = 1
    for char in probas:
        probas[char] /= len(text)
    return probas

def code_huffman(text, source_code_path):
    probas = calculate_proba(text)
    symboles = []
    for char in probas:
        symboles.append(
            Symbole(
                label=char,
                proba=probas[char],
                left_previous=None,
                right_previous=None,
                left_arete=None,
                right_arete=None,
                code=None
            )
        )
    S = Source(symboles)
    huffman = S.huffman()
    write_source_code(source_code_path, huffman)

    binary = ''
    for char in text:
        binary += next(symbole.code for symbole in huffman if symbole.label == char)
    # print("Binary initial : ", len(binary))
    return binary

def compress(input_file_path, output_file_path, source_code_path):
    text = read_file(input_file_path)
    binary = code_huffman(text, source_code_path)
    # print("Binary final : ", len(format_8(binary)))
    write_bytes(output_file_path, format_8(binary))

def decode_huffman(binary, source_code_path):
    huffman = read_source_code(source_code_path)
    nombre = read_file('nombre.txt')
    print("Nombre 0 = ", nombre)
    text = ''
    test_code = ''
    for i in range(len(binary) - (int(nombre))):
        test_code += binary[i]
        for symbole in huffman:
            if test_code == symbole.code:
                text += symbole.label
                test_code = ''
                break
    return text

def decompress(input_file_path, output_file_path, source_code_path):
    binary = read_bytes(input_file_path)
    text = decode_huffman(binary, source_code_path)
    write_file(output_file_path, text)