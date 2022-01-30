import random

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

verb_noun_list = [
    'act', 'address', 'aim', 'answer', 'back', 'balloon', 'bank',
    'battle', 'bear', 'bend', 'blast', 'block', 'break', 'brush',
    'catch', 'challenge', 'charge', 'cheer', 'color', 'cook',
    'crack', 'curl', 'cycle', 'dance', 'design', 'die', 'divorce',
    'double', 'doubt', 'dust', 'echo', 'end', 'estimate', 'face',
    'finish', 'fish', 'flood', 'fool', 'frown', 'garden', 'glue',
    'guard', 'guess', 'hammer', 'hand', 'head', 'hug', 'joke',
    'kick', 'kiss', 'laugh', 'loan', 'love', 'man', 'march',
    'milk', 'name', 'number', 'object', 'order', 'paddle', 'peel',
    'permit', 'play', 'pop', 'practice', 'produce', 'punch',
    'question', 'quiz', 'rhyme', 'rock', 'roll', 'run', 'sand',
    'saw', 'skate', 'smell', 'surprise', 'thunder', 'tie', 'time',
    'toast', 'trace', 'train', 'treat', 'trick', 'use', 'vacuum',
    'value', 'visit', 'wake', 'walk', 'water', 'wish', 'work',
    'x-ray', 'yawn', 'zone'
    ]

noun_list = [
    'time', 'year', 'people', 'way', 'day', 'man', 'thing', 'woman',
    'life', 'child', 'world', 'school', 'state', 'family', 'student',
    'group', 'country', 'problem', 'hand', 'part', 'place', 'case',
    'week', 'company', 'system', 'program', 'question', 'work', 'government',
    'number', 'night', 'point', 'home', 'water', 'room', 'mother', 'area',
    'money', 'story', 'fact', 'month', 'lot', 'right', 'study', 'book',
    'eye', 'job', 'word', 'business', 'issue', 'side', 'kind', 'head', 'house',
    'service', 'friend', 'father', 'power', 'hour', 'game', 'line', 'end', 'member',
    'law', 'car', 'city', 'community', 'name', 'president', 'team', 'minute',
    'idea', 'kid', 'body', 'information', 'back', 'parent', 'face', 'others',
    'level', 'office', 'door', 'health', 'person', 'art', 'war', 'history', 'party',
    'result', 'change', 'morning', 'reason', 'research', 'girl', 'guy', 'moment',
    'air', 'teacher', 'force', 'education'
]


for index in range(10):
    print('The ' + random.choice(adjective_noun_list) + ' ' + random.choice(verb_noun_list) + ' the ' +  random.choice(noun_list))
