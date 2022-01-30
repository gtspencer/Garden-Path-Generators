from nltk import CFG, ChartParser
from random import choice
import nltk
from nltk.corpus import gutenberg

def produce(grammar, symbol):
    words = []
    productions = grammar.productions(lhs = symbol)
    production = choice(productions)
    for sym in production.rhs():
        if isinstance(sym, str):
            words.append(sym)
        else:
            words.extend(produce(grammar, sym))
    return words

grammar = CFG.fromstring('''
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I' | 'me'
VP -> V NP | VP PP
V -> 'shot' | 'killed' | 'wounded'
Det -> 'a' | 'an' | 'my'
N -> 'elephant' | 'pajamas' | 'cat' | 'dog'
P -> 'in' | 'outside'
''')

parser = ChartParser(grammar)

gr = parser.grammar()
# print(' '.join(produce(gr, gr.start())))

adjective_noun_list = [
    'abstract, alert', 'antique', 'average', 'back', 'brief',
    'base', 'best', 'better', 'chief', 'classic', 'clear', 'close', 'cold', 'compact',
    'complex', 'content', 'cool', 'cooler', 'dear', 'deep', 'down', 'evil', 'expert',
    'fair', 'fake', 'fancy', 'fast', 'fat', 'female', 'few', 'fine', 'firm', 'first',
    'flat', 'fleet', 'good', 'grave', 'green', 'gross', 'half', 'high','hollow', 'hurt',
    'ideal', 'ill', 'intent', 'invalid', 'joint', 'juvenile', 'key', 'kind', 'last',
    'left', 'light', 'lighter', 'limp', 'liquid', 'major', 'male', 'mean', 'minute',
    'novel', 'number', 'orange', 'oval', 'phony', 'present', 'prime', 'prize', 'rank',
    'rash', 'rear', 'right', 'round', 'safe', 'sage', 'second', 'set', 'sharp',
    'sore', 'sound', 'spare', 'split', 'square', 'stable', 'static', 'still',
    'straight', 'stray', 'suspect', 'tart', 'tender', 'terminal', 'token', 'total',
    'trial', 'upset', 'well'
    ]

string = ''
for s in adjective_noun_list:
    string += '\'' + s + '\'' + ' | '

#grammarString = """
#S -> NP VP
#PP -> P NP
#NP -> Det Adj N | Det Adj N PP | Det N | Det N PP | 'I'
#VP -> V NP | VP PP
#Det -> 'an' | 'my' | 'the' | 'a'
#N -> 'elephant' | 'pajamas' | 'complex' | 'garden' | """
#grammarString += string
#grammarString += """
#Adj -> 'green' | 'tart'
#V -> 'shot' | 'garden'
#P -> 'in'
#"""

# use this grammar with the above code (# print(' '.join(produce(gr, gr.start()))))) and input the parsed grammar lists after N, Adj, and V

gardenPathGrammar = """
S -> NP VP
PP -> P NP
NP -> Det Adj N | Det Adj N PP | Det N | Det N PP
VP -> V NP | VP PP | V
Det -> 'an' | 'the' | 'a'
N -> 'elephant' | 'pajamas' | 'complex' | 'garden' | 'tart'
Adj -> 'green' | 'tart'
V -> 'shot' | 'garden'
P -> 'in'
"""

groucho_grammar = nltk.CFG.fromstring(gardenPathGrammar)


sent = ['I', 'shot', 'a', 'green', 'elephant', 'in', 'my', 'pajamas']
sent = ['the', 'tart', 'garden', 'the', 'elephant']
sentence = 'The complex houses married and single soldiers and their families'
split = sentence.split(' ')
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    print(tree)


#nltk.download('gutenberg')
#nltk.download('punkt')


#bible = gutenberg.words(u'bible-kjv.txt')
#bibleText = nltk.Text(bible)
#print(bibleText)
#print(type(bible))
#bibleText.generate()


#mobyDick = nltk.Text(text1)
#print(text1)
#mobyDick.generate()
