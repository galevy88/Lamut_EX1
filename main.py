from USRR import USRR
from RT import RT
from TRANSLATE import TRANSLATE
import sys

if __name__ == '__main__':
    dna_usrr = sys.argv[1]
    rna_rt = sys.argv[2]
    rna_translate = sys.argv[3]
    rf = sys.argv[4]

    
    usrr = USRR(dna_usrr)
    SRRs = usrr.find_all_srr()
    if(SRRs != ""):
        print(SRRs)
    else:
        print("No simple repeats in DNA sequence")

    rt = RT(rna_rt)
    dna_sequence = rt.reverse_transcrive()
    print(f"DNA sequence: {dna_sequence}")

    translte = TRANSLATE(rna_translate, rf)
    protein = translte.translate()
    if(protein != ""):
        print(f"Translation: {protein}")
    else:
        print("Non-coding RNA")

    # dna_usrr = 'ATCA'
    # rna_rt = 'AUcaaG'
    # rna_translate = 'AUGCAUGAACUAGAUGAACAUGCAGAUCUAACGUG'
    # rf = 1