class Section():
    def __init__(self, name):
        self.words = {}      # Dictionary of words
        self.name = name     # Name of section
        
    def getWords(self):
        return self.words
    
    def getName(self):
        return self.name
    
    def addWord(self, key, w):
        self.words[key] = w
        
    def __str__(self):
        return f'Words: {self.words}\nFound: {self.found}'
    
    
class Word():
    def __init__(self, word):
        self.word = word       # Word
        self.likeCount = 0     # Total likes
        
    def setlikeCount(self, likes):
        self.likeCount += likes
        
    def getWord(self):
        return self.word
    
    def getlikeCount(self):
        return self.likeCount
    
    def __str__(self):
        return f'Words: {self.word}\nLike Count: {self.likeCount}'
     
        
sectionDict = {}
e = Section('Horray')

f = Word('Test')

sectionDict[e.getName()] = e

sectionDict['Horray'].addWord('Test', f)
sectionDict['Horray'].words['Test'].setlikeCount(15)
print(sectionDict['Horray'].words['Test'])
