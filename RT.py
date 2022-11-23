




class RT:
    def __init__(self, RNA):
        self.dict = { "u" : "A",
                      "U" : "A",
                      "a" : "T",
                      "A" : "T",
                      "c" : "G",
                      "C" : "G",
                      "g" : "C",
                      "G" : "C",
                      }
        self.RNA = RNA
    
    
    def reverse_transcrive(self):
        ls = []
        dna = []
        for r in self.RNA:
            ls.append(self.dict[r])
        while ls:
            dna.append(ls.pop())
        dna_str = ""
        for d in dna:
            dna_str += d
        return dna_str