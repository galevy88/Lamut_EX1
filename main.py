
from USRR import USRR
from RT import RT



if __name__ == '__main__':
    dna_usrr = 'AAAATAGTAGTAGTAGTAGTAGTATGATATGATATGATAGGACCCCAGGGACGCCATTTTACCCCCAGGGAGCGCAGGCGCGCGCGCAGCGCAGCTACTATACTGCTGCGACTGCCTTCTCTACTACTACTCGACATCTAC'
    usrr = USRR(dna_usrr)
    SRR_list = usrr.find_all_srr()
    print(SRR_list)

    rna_rt = 'AUcaaG'
    rt = RT(rna_rt)
    ls = rt.reverse_transcrive()
    print(ls)

