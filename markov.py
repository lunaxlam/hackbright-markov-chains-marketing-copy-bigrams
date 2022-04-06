"""Generate Markov text from text files."""

# From the "random" library import only the "choice" function
from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Open file as a file object called "f" and read the contents of the file
    with open (file_path, 'r') as f:
        # Store the read file contents as a single string object
        text_string = f.read()

    return text_string


def make_chains(text_string):
    """Take input text (corpus) as string; return dictionary of Markov chains.

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
    # Initialize an empty dictionary to store the chains of bigram tuple (key), subsequent word (value) pairs
    chains = {}

    # Tokenize the file string object into a list using an empty delimiter argument to split the string object by any space
    words = text_string.split()

    # Iterate through the list of words up to the second-to-last element
    for i in range(len(words)-2):

        # Check to see if bigram as a type(tuple) key already exists in the dictionary
        # If the bigram does not already exist in the dictionary then initialize the bigram tuple and set = to the element at the third index
        # The element at the third index is relative to the current "i" element that is being iterated over
        if (words[i], words[i+1]) not in chains:
            chains[(words[i], words[i+1])] = [words[i+2]]   
        else:
            # If the bigram does already exist in the dictionary then update the value by adding to the existing list of values
            # We will add the element at the third index that is relative to the current "i" element that is being iterated over
            chains[(words[i], words[i+1])] += [words[i+2]]

            # # Note: .append() method works here, too!
            # chains[(words[i], words[i+1])].append(words[i+2])

    return chains


def make_text(chains):
    """Return text from chains."""

    # Initialize an empty to list to join as a string to return 
    words = []

    # Get a random key
    random_key = choice(list(chains.keys()))

    # Append a random value from the random key to our list of words
    words.append(choice(chains[random_key]))

    # Store the second to last word in the previous key
    last_key = random_key[1]

    # Repeat until a KeyError is encountered
    while True:
        
        try:

            # Create the new key
            new_key = (last_key, words[-1])
            # Append a random value from the new key to our list of words
            words.append(choice(chains[new_key]))
            # Update last_key
            last_key = new_key[1]
        
        except KeyError:
            # Break out of the loop
            break
    
    # Join the elements in the list of words as a string and separate element with a single whitespace
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
