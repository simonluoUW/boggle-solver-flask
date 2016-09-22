'''
represents a Trie at root
- contains method to add words to the trie
'''
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

'''
node in Trie
- word is not None if node represents a word
- children dictionary
    key is next letter in word
    value is the next TrieNode for that letter
'''
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = dict()


# Returns a trie of words in boggle_dict.txt
def build_trie():
    trie = Trie()
    with open("boggle_dict.txt", "r") as file:
        for line in file:
            word = line.rstrip('\n')
            trie.add_word(word)
    return trie

