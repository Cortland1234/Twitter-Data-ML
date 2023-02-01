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
        return f'Words: {self.words}\nFound: {self.found}'
    
    
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
     
        
sectionDict = {}

# Example of making section class
e = Section('Horray')

# Example of making word class
f = Word('Test')

# Example of adding section to section dictionary
sectionDict[e.getName()] = e

# Example of adding word to section dictionary
sectionDict['Horray'].addWord('Test', f)

# Example of setting like count for specific word in specific section
sectionDict['Horray'].words['Test'].setlikeCount(15)

# Example of incrementing global like count for specific section
sectionDict['Horray'].incLikes(sectionDict['Horray'].words['Test'].getlikeCount())

# Print Examples
print(sectionDict['Horray'].words['Test'])
print(sectionDict['Horray'].gettotalLikes())