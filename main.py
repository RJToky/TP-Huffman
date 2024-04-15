from huffman import Source, Symbole
from utils import *

def main():
    # symboles = [
    #     Symbole(label="A", proba=0.30, left_previous=None, right_previous=None, left_arete=None, right_arete=None, code=None),
    #     Symbole(label="B", proba=0.15, left_previous=None, right_previous=None, left_arete=None, right_arete=None, code=None),
    #     Symbole(label="C", proba=0.15, left_previous=None, right_previous=None, left_arete=None, right_arete=None, code=None),
    #     Symbole(label="D", proba=0.20, left_previous=None, right_previous=None, left_arete=None, right_arete=None, code=None),
    #     Symbole(label="E", proba=0.10, left_previous=None, right_previous=None, left_arete=None, right_arete=None, code=None),
    #     Symbole(label="F", proba=0.10, left_previous=None, right_previous=None, left_arete=None, right_arete=None, code=None),
    # ]
    # source = Source(symboles)
    # huffman = source.huffman()
    # for symbole in huffman:
    #     print(f"Symbole: {symbole.label} - Code: {symbole.code}")

    compress("./file/genesis.txt", "./bin/genesis.bin", "./source/genesis.pkl")
    # decompress("./bin/genesis.bin", "./file/genesis.txt", "./source/genesis.pkl")
    pass

if __name__ == "__main__":
    main()