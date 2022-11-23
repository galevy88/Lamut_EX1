
class USRR:
    def __init__(self, DNA):
        self.check_input(DNA)
        self.DNA = DNA
        self.frontier = []
        self.SRR = {}

    def check_input(self, dna):
        for d in dna:
            if (d != 'A' and d !='C' and d != 'G' and d !='T'):
                print("Invalid DNA Input")
                exit()
    
    def find_srr_one_time(self,dna, sr, s):
        work_dna = dna[s:]
        self.frontier = self.split(work_dna, sr)
        strike = 1
        while self.frontier:
            current = self.frontier.pop(0)
            if self.frontier != []:
                if (current == self.frontier[0]):
                    strike += 1
                else: strike = 1
            if strike >= 3:
                self.SRR[current] = strike
        

    def find_all_srr(self):
        srr_size = [1, 2, 3, 4, 5, 6]
        for sr in srr_size:
            for s in range(0, sr):
                cp_dna = self.DNA
                self.find_srr_one_time(cp_dna, sr , s)
        ls = self.create_ls(self.SRR)
        return self.parser(ls)
    
    def split(self, worked_dna, sr):
        ls = [worked_dna[i:i+sr] for i in range(0, len(worked_dna), sr)]
        return ls

    def create_ls(self, dict):
        ls = []
        for key in dict:
            ls.append((key, dict[key]))
        return ls
    
    def parser(self, list):
        str = ""
        for srr in list:
            str += f"{srr[0]},{srr[1]};"
        return str[:-1]
            

