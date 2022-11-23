
class TRANSLATE:
    def __init__(self, RNA, rf):
        self.codons = {
            "UUU" : "F", "UCU" : "S", "UAU" : "Y", "UGU" : "C", 
            "UUC" : "F", "UCC" : "S", "UAC" : "Y", "UGC" : "C",
            "UUA" : "L", "UCA" : "S", "UAA" : "X", "UGA" : "X",
            "UUG" : "L", "UCG" : "S", "UAG" : "X", "UGG" : "W",
            "CUU" : "L", "CCU" : "P", "CAU" : "H", "CGU" : "R",
            "CUC" : "L", "CCC" : "P", "CAC" : "H", "CGC" : "R",
            "CUA" : "L", "CCA" : "P", "CAA" : "Q", "CGA" : "R",
            "CUG" : "L", "CCG" : "P", "CAG" : "Q", "CGG" : "R",
            "AUU" : "I", "ACU" : "T", "AAU" : "N", "AGU" : "S",
            "AUC" : "I", "ACC" : "T", "AAC" : "N", "AGC" : "S",
            "AUA" : "I", "ACA" : "T", "AAA" : "K", "AGA" : "R",
            "AUG" : "M", "ACG" : "T", "AAG" : "K", "AGG" : "R",
            "GUU" : "V", "GCU" : "A", "GAU" : "D", "GGU" : "G",
            "GUC" : "V", "GCC" : "A", "GAC" : "D", "GGC" : "G",
            "GUA" : "V", "GCA" : "A", "GAA" : "E", "GGA" : "G",           
            "GUG" : "V", "GCG" : "A", "GAG" : "E", "GGG" : "A"
        }
        self.rf = int(rf)
        self.RNA = RNA[self.rf-1:]

    
    def choose_protein_to_return(self, Proteins):
        size = 0
        chosen_p = ""
        for p in Proteins:
            if len(p) > size:
                size = len(p)
                chosen_p = p
        return chosen_p


    def translate(self):
        Proteins = []
        protein = ""
        RNA = [self.RNA[i:i+3] for i in range(0, len(self.RNA), 3)]
        is_translating = False
        for codon in RNA:
            if(len(codon) == 3):
                if(codon == 'AUG'):
                    is_translating = True
            if is_translating and self.codons[codon] == "X":
                is_translating = False
                Proteins.append(protein[:-1])
                protein = ""
            if(is_translating):
                protein += self.codons[codon] + ';'
        return self.choose_protein_to_return(Proteins)