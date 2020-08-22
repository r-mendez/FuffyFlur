import random

"""Function to open, read, and import from list of text files and convert to tuples."""
def getWords(filename):
    files = open(filename)
    temp_list = list()
    for each_line in files:
        each_line = each_line.strip()
        temp_list.append(each_line)

    words = tuple(temp_list)
    files.close()

    return words

"""Imports random words from the text files."""
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
articles = getWords('articles.txt')
prepositions = getWords('prepositions.txt')
conjunctions = getWords('conjunctions.txt')
adjectives = getWords('adjectives.txt')

"""Builds sentence."""
def sentence():    
    return nounPhrase() + " " + verbPhrase() + "."

"""Returns a noun phrase."""
def nounPhrase():   
    return random.choice(articles) + " " + random.choice(adjectives) + " " + random.choice(nouns) 

"""Returns a verb phrase."""
def verbPhrase():    
    prepphrase = ""
    prepchance = random.randrange(101) + 1
    if(prepchance > 70):
        prepphrase = prepositionalPhrase()
    return random.choice(verbs) + " " + nounPhrase() + " " + prepphrase

"""Returns a prepositional phrase with a conjunction."""
def prepositionalPhrase():
    conjphrase = ""
    conjchance = random.randrange(100) + 1
    if (conjchance > 90):
        conjphrase = conjunctionPhrase()
    return random.choice(prepositions) + " " + random.choice(articles) + " " + conjphrase + " " + nounPhrase() + " " + verbPhrase()

"""Connects an adjective phrase."""
def AdjectivePhrase():    
    return random.choice(adjectives) + " " + verbPhrase() + " " + conjunctions + " " + nounPhrase()

"""Optional conjunctional phrase."""
def conjunctionPhrase():
    adjphrase = ""    
    adjchance = random.randrange(100)+1
    if (adjchance > 70):
        adjphrase = AdjectivePhrase()
    return random.choice(conjunctions) + " " + random.choice(adjectives) + " " + random.choice(articles) + " " + nounPhrase() + " " + adjphrase

"""Asks the user for number of sentences to be generated."""
def main():    
    number = int(input('Number of sentences to be generated: '))
    print (" ")
    print("Sentences generated: \n")
    for count in range(number):
        print(sentence())

if __name__=='__main__':
    main()
