"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    poem = open(file_path).read()
    #print(poem)

    return poem

#print(open_and_read_file('green-eggs.txt'))

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
    

    # your code goes here
    words = text_string.split()
    # print(line)

# Would, you, could, you, in, a house?, Would, you could you with a mouse?

    for i in range(len(words) - 2):
        pairs = (words[i], words[i + 1]) # [0], [1]
        
        if pairs in chains:
        
            chains[pairs].append(words[i + 2]) #[2]
            #chains.get(pairs)
        else:
            chains[pairs] = [words[i + 2]]
            # print(chains[pairs])
    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    #for key, value in chains:
        # print(key)
        #random_text = choice(chains.key())
        #print(random_text)
    
        # print(value)
        
    #print(chains)
    
    #chains[keys]= values
    random_text_key = choice(list(chains.keys()))
    # print(f'this is random text key: {random_text_key}')
    random_text_value = choice(chains[random_text_key])

    words.extend([random_text_key[0], random_text_key[1], random_text_value])
    #[('would', 'you')] => ['would', 'you']
    """
    1. Make a new key out of the second word in the first key and the 
        random word you pulled out from the list of words that followed it.
    2. Look up that new key in the dictionary, and pull a new random word 
        out of the new list.
    3. Keep doing that until your program raises a KeyError.

    We used choice() to get (and, ham?) to start our "story"
    Used choice() to pick what comes next based on (and, ham?)

    words = [and, ham?, Would]
    Go use (ham?, Would) to find the next word by doing choice()
    """

    while True:

        two_word_story = (words[-2], words[-1])
        # ^ is (ham?, Would)
      
        # print(two_word_story)
        # print(one_word_story)
        
        
        # if one_word_story == "am?":
        #     break
        #     
        if two_word_story in chains:
            one_word_story = choice(chains[two_word_story])
            words.extend([one_word_story])
        else:
            break
        # elif two_word_story == choice(list(chains.keys())) and one_word_story = choice(chains[random_text_key]):                   
        #     words.extend([two_word_story[0], random_text_key[1], random_text_value])

    
   
    return ' '.join(words)



input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
