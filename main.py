# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string
def read_file_content(filename):
    text = open (filename, 'r' )
    return text.read()
    # [assignment] Add your code here 
    
    


def count_words():
    text = read_file_content("./story.txt")
    new_str = text.translate(str.maketrans('','', string.punctuation))
    counts = dict()
    words = new_str.split()
    # [assignment] Add your code here

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print (counts)

count_words ()
         
