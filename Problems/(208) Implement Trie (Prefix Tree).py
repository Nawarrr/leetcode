# Question Link
# https://leetcode.com/problems/implement-trie-prefix-tree/

# Description
'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 
'''

class Node:
    def __init__(self):
        self.children = {}
        self.endWord = False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr  = self.root
        for i in word:
            if i not in curr.children.keys():
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.endWord = True
    def search(self, word: str) -> bool:
        curr = self.root
        i = 0
        while i < len(word):
            if word[i] not in curr.children.keys():
                return False
            else:
                curr = curr.children[word[i]]
                i+=1
        #print(curr.children)
        if curr.endWord :
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        i = 0
        while i < len(prefix):
            if prefix[i] not in curr.children.keys():
                return False
            else:
                curr = curr.children[prefix[i]]
                i+=1
                
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)