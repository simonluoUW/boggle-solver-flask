class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self,word):
        cur = self.root
        for character in word:
            if character not in cur.children:
                cur.children[character] = TrieNode()
            cur = cur.children[character]
        cur.word = word


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = dict()


def build_trie():
    trie = Trie()
    with open("boggle_dict.txt", "r") as file:
        for line in file:
            word = line.rstrip('\n')
            trie.add_word(word)
    return trie

