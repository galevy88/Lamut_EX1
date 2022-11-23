
from USRR import USRR
from RT import RT
from TRANSLATE import TRANSLATE



if __name__ == '__main__':
    dna_usrr = 'ATCA'
    usrr = USRR(dna_usrr)
    SRRs = usrr.find_all_srr()
    if(SRRs != ""):
        print(SRRs)
    else:
        print("No simple repeats in DNA sequence")

    rna_rt = 'AUcaaG'
    rt = RT(rna_rt)
    ls = rt.reverse_transcrive()
    print(ls)

    rna_translate = 'AUGAUGAUGUGA'
    translte = TRANSLATE(rna_translate, 1)
    protein = translte.translate()
    if(protein != ""):
        print(protein)
    else:
        print("Non-coding RNA")
