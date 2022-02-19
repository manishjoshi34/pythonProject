from gc import collect
from logging import root


class TrieNode:
    def __init__(self,chr) -> None:
        self.chr = chr
        self.child = {}
        self.isWord = False
        self.count = 0
    def __str__(self) -> str:
        strdata = str(self.chr)
        strdata = strdata + str(self.child)
    def addChild(self,node):
        if self.getChild(node) == None:
            self.child[node] = TrieNode(node)
        return self.child[node]
    def getChild(self,key):
        if key in self.child.keys():
            return self.child[key]
        return None
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("");
    def __str__(self):
        return str(self.root)
    def addWord(self, word):
        temp = self.root
        for i in range(0,len(word),1):
            temp = temp.addChild(word[i]);
            if i == len(word)-1:
                temp.isWord = True
                temp.count+=1
    def collect(self,collectName,collectDict, node):
        collectName.append(node.chr)
        if node.isWord : 
            word = "".join(collectName)
            if word in collectDict.keys():
                collectDict[word] +=node.count
            else:
                collectDict[word] = node.count
        
        for n in node.child.values():
            self.collect(collectName,collectDict,n)
        collectName.pop()
    def find(self,word):
        temp = self.root
        for idx in range(0,len(word),1):
            if word[idx] in temp.child.keys():
                temp = temp.child[word[idx]]
                if idx == len(word)-1:
                    if temp.isWord:
                        return True
                    else:
                        return False
            else:
                return False
    
    def print(self):
        collectName = []
        collectDict = {}
        self.collect(collectName,collectDict,self.root)
        print(collectDict)
        
def main():
    T = Trie()
    T.addWord("manish")
    T.addWord("man")
    T.addWord("manage")
    T.addWord("manish")
    T.print() 
    print(T.find("hetal"))
    print(T.find("man"))
    print(T.find("manish"))
    
    
if __name__=='__main__':
    main()
        