"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    
    for i in range(len(words) - 2):
        # print(words[i], words[i + 1])
        if (words[i], words[i + 1]) not in chains: 
            chains[(words[i], words[i + 1])] = [words[i + 2]]
        else:
            chains[(words[i], words[i + 1])].append(words[i + 2])

    return chains


def make_text(chains):
    """Return text from chains."""

    #create variable for initial tuple (the "link")
    #add each word in our_string to the words list
    #create a while our_string is in chains
        #adding the randomly chosen value to words list
        #creating new variable for our_string with last item in tuple and random value 
    words = []
    our_string = ("could", "you")
    # current_key = chains.choice()
    for word in our_string: 
        words.append(word)

    while our_string in chains:
        random_word = choice(chains[our_string])
        words.append(random_word)
        our_string = (our_string[1], random_word)
        
    return ' '.join(words)
   
input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)









    # words = []
    # current_key = ("could", "you")
    # for word in current_key:
    #     words.append(word)

    # while current_key in chains: 
    #     chosen_word = choice(chains[current_key])
    #     new_key = (current_key[1], chosen_word)
    #     words.append(chosen_word)
    #     current_key = new_key

    # return " ".join(words)
