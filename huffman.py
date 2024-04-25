import math

class Symbole:
    def __init__(self, label, proba, left_previous, right_previous, left_arete, right_arete, code) -> None:
        self.label = label
        self.proba = proba
        self.left_previous = left_previous
        self.right_previous = right_previous
        self.left_arete = left_arete
        self.right_arete = right_arete
        self.code = code
    
    def set_arete(self):
        if self.left_previous:
            self.left_arete = '1'
            self.left_previous.set_arete()
        if self.right_previous:
            self.right_arete = '0'
            self.right_previous.set_arete()
        return self
    
    def set_code(self):
        if self.left_previous:
            if not self.code:
                self.code = ''
            self.left_previous.code = self.code + '' + self.left_arete
            self.left_previous.set_code()

        if self.right_previous:
            if not self.code:
                self.code = ''
            self.right_previous.code = self.code + '' + self.right_arete
            self.right_previous.set_code()
        return self
    
    def get_leaves(self):
        leaves = []
        if not self.left_previous and not self.right_previous:
            leaves.append(self)
        if self.left_previous:
            leaves.extend(self.left_previous.get_leaves())
        if self.right_previous:
            leaves.extend(self.right_previous.get_leaves())
        return leaves

class Source:
    def __init__(self, symboles) -> None:
        self.symboles = symboles

    def union_symboles(self):
        if(len(self.symboles) == 1):
            return self.symboles[0]
        
        symboles_sorted = sorted(self.symboles, key=lambda e: e.proba)
        symbole_1 = symboles_sorted.pop(0)
        symbole_2 = symboles_sorted.pop(0)
        
        new_source = Source(symboles_sorted.copy())

        new_symbole = Symbole(
            label=symbole_1.label+symbole_2.label,
            proba=symbole_1.proba+symbole_2.proba,
            left_previous=symbole_1,
            right_previous=symbole_2,
            left_arete=None,
            right_arete=None,
            code=None
        )

        new_source.symboles.append(new_symbole)
        return new_source.union_symboles()

    def huffman(self):
        tree = self.union_symboles()
        tree = tree.set_arete()
        tree = tree.set_code()
        leaves = tree.get_leaves()

        q = 2
        # print("Proba = ", Source.total_proba(leaves))
        print("H(S) = ", Source.entropie(leaves) / math.log(q, 2))
        print("NC = ", Source.nc(leaves))
        print("H(S) + 1 = ", (Source.entropie(leaves) / math.log(q, 2)) + 1)

        return leaves

    @staticmethod
    def entropie(symboles):
        rep = 0
        for symbole in symboles:
            rep += symbole.proba * math.log(symbole.proba, 2)
        return -1 * rep
    
    @staticmethod
    def nc(symboles):
        rep = 0
        for symbole in symboles:
            rep += symbole.proba * len(symbole.code)
        return rep
    
    @staticmethod
    def total_proba(symboles):
        rep = 0
        for symbole in symboles:
            rep += symbole.proba
        return rep