class Section():
    def __init__(self, name):
        self.words = {}      # Dictionary of words
        self.name = name     # Name of section
        self.totalLikes = 0  # Total Likes for section
        
    def getWords(self):
        return self.words
    
    def getName(self):
        return self.name
    
    def gettotalLikes(self):
        return self.totalLikes
    
    def addWord(self, key, w):
        self.words[key] = w
        
    def incLikes(self, wLikes):
        self.totalLikes += wLikes
        
    def __str__(self):
        return f'Words: {self.words}'
    
    
class Word():
    def __init__(self, word):
        self.word = word       # Word
        self.likeCount = 0     # Total likes for word
        
    def setlikeCount(self, likes):
        self.likeCount += likes
        
    def getWord(self):
        return self.word
    
    def getlikeCount(self):
        return self.likeCount
    
    def __str__(self):
        return f'Words: {self.word}\nLike Count: {self.likeCount}'