import json
from itertools import permutations

# Load words from JSON file
with open('words_dictionary.json', 'r') as file:
    data = json.load(file)
    word_set = set(word for word in data if len(word) >= 4)

def filter_words(input_str):
    result = set()
    for length in range(len(input_str), 0, -1):
        # Generate all permutations of length 'length'
        perms = [''.join(perm) for perm in permutations(input_str, length)]
        
        # Convert permutations to a set for faster filtering
        perm_set = set(perms)
        
        # Filter words by length and update result set
        result.update(word for word in perm_set if len(word) >= 4 and word in word_set)
    
    return result

while(True):
    # Input string of letters
    input_string = input("Enter letters: ").lower()

    # Filter and print words
    filtered_words = sorted(filter_words(input_string), key=len, reverse=True)
    print(filtered_words)
