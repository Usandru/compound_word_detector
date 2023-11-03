import marisa_trie
from typing import List

class MorphemeTrie:
    def __init__(self, morpheme_list : List[str]) -> None:
        self.trie = marisa_trie.Trie(morpheme_list)

    def find_compounds(self, word : str) -> List[List[str]]:
        prefixes = self.trie.prefixes(word)
        results = []
        if len(prefixes) == 0:
            return None
        for prefix in prefixes:
            if len(prefix) == len(word):
                results.append([prefix])
            else:
                suffixes = self.find_compounds(word[len(prefix):])
                if suffixes != None:
                    for suffix in suffixes:
                        results.append([prefix] + suffix)
        if len(results) == 0:
            return None
        else:
            return results
