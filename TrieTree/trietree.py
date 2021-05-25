# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         trietree
# Description:  构建一个字典树
# Author:       zhaomengyi
# Date:         2021/5/19
# NO:LC208
#-------------------------------------------------------------------------------
class Trie:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = {}
    self.end_of_word = "#"

  def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
    node = self.root
    for char in word:
      node = node.setdefault(char,{})
    node[self.end_of_word] = self.end_of_word

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    """
    node = self.root
    for char in word:
      if char not in node:
        return False
      node = node[char]
    return self.end_of_word in node and len(node) == 1


  def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    node = self.root
    for char in prefix:
      if char not in node:
        return False
      node = node[char]
    return True

# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':

  trie = Trie()
  trie.insert("apple");
  a=trie.search("apple");   # 返回 True
  b=trie.search("app");     # 返回 False
  c=trie.startsWith("app"); # 返回 True
  d=trie.insert("app");
  e=trie.search("app");     # 返回 True

