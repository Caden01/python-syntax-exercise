def print_upper_words(words) :
    """Prints out each word in all uppercase in superate lines"""

    """print_upper_words(["hello", "hey", "goodbye", "yo", "yes"]) should print
        HELLO 
        HEY
        GOODBYE
        YO
        YES
    """
    
    for word in words :
        print(word.upper())

def print_upper_words2(words) :
    """Prints each word in all uppercase on a separate line if it starts with e or E"""

    """print_upper_words2(["Elephant", "hi", "empty"]) should print 
        ELEPHANT
        EMPTY
    """

    for word in words :
        if word[0] == "e" or word[0] == "E" :
            print(word.upper())

def print_upper_words3(words, must_start_with) :
    """Prints each word in all uppercase on a seperate line if starts with any of the given letters"""

    """print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"]) should print 
        HELLO
        HEY
        YO
        YES
    """

    for word in words :
        if word[0] in must_start_with :
            print(word.upper())
    

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words2(["Elephant", "hi", "empty"])
print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"])