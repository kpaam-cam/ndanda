from lingpy import *
from lingpy.compare.partial import Partial

def run(wordlist):

    D = {0: [c for c in wordlist.columns]}
    for idx in wordlist:
        D[idx] = [entry for entry in wordlist[idx]]

    lex = Partial(D)
    lex.partial_cluster(
            method="sca", ref="cogids", threshold=0.45,
            cluster_method="infomap")
    alms = Alignments(lex, ref="cogids")
    alms.align()
    C = {idx: lex[idx, "cogids"] for idx in lex}
    wordlist.add_entries("cogids", C, lambda x: x)
    C = {idx: alms[idx, "alignment"] for idx in lex}
    wordlist.add_entries("alignment", C, lambda x: x)
    return wordlist
