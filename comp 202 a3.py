# Anjali Ravi, 261159848

import doctest
#doctest.testmod()

LEFT_DIRECTION = -1
RIGHT_DIRECTION = 1

def is_outside_list(letter_list, index):
    '''
    (list, int) -> bool
    Takes a list of letters and an integer and returns true if index is
    negative or out of list
    >>> is_outside_list(['A', 'B', 'C', 'D'], 4)
    True
    >>> is_outside_list(['A', 'B', 'C', 'D'], 0)
    False
    >>> is_outside_list(['A', 'B', 'C', 'D'], -1)
    True
    '''
    list_length = len(letter_list)
    
    if 0 <= index and index < list_length: #Checking if index is in list
        return False
    else:
        return True
    

def letter_positions(letter_list, character):
    '''
    (list, str) -> list
    Takes a list of letters and a character and returns a list of the indices
    where this character appears in the list
    >>> letter_positions(['A', 'B', 'C', 'D'], 'A')
    [0]
    >>> letter_positions(['A', 'B', 'C', 'D', 'A'], 'A')
    [0, 4]
    >>> letter_positions(['A', 'B', 'C', 'D', 'A'], 'M')
    []
    '''
    positions = []
    i = 0
    while i <= len(letter_list) - 1:
        if letter_list[i] == character: #Checks if element is equal to char
            positions.append(i) #Adds to list to return if equal
            i += 1
        else:
            i += 1
    
    return positions


def valid_word_pos_direction(letter_list, word, index, direction):
    '''
    (list, str, int, int) -> Bool
    Returns true if word is ound at given location and direction in list,
    returns false if not
    >>> valid_word_pos_direction(['A', 'B', 'C', 'D', 'C', 'M'], 'BAD', 1, 1)
    False
    >>> valid_word_pos_direction(['A', 'B', 'C', 'D', 'C', 'M'], 'DCB', 3, -1)
    True
    >>> valid_word_pos_direction(['A', 'B', 'C', 'D', 'C', 'M'], 'MAB', 5, 1)
    False
    '''
    
    for element in word:
        if is_outside_list(letter_list, index) == True:
            #Checks if index is out of list
            return False
        if element != letter_list[index]:
            #Checks if letter is same as letter in list
            return False
        index += direction #increases/decreases index    
        
    return True


def direction_word_given_position(letter_list, word, index):
    '''
    (list, str, int) -> list
    Returns a list of directions that a word is found in a list
    >>> direction_word_given_position(['A', 'B', 'C', 'D', 'C', 'M'],
    'DCM', 3)
    [1]
    >>> direction_word_given_position(['A', 'B', 'C', 'D', 'C', 'M'], 'DC', 3)
    [-1, 1]
    >>> direction_word_given_position(['A', 'B', 'C', 'D', 'C', 'M'], 'L', 3)
    []
    '''
    word_directions = []
    
    if valid_word_pos_direction(letter_list, word, index, LEFT_DIRECTION) ==\
    True:
        word_directions.append(-1)
        
    if valid_word_pos_direction(letter_list, word, index, RIGHT_DIRECTION) ==\
    True:
        word_directions.append(1)
    
    return word_directions


def position_direction_word(letter_list, word):
    '''
    (list, str) -> list
    Takes list of letters and a word and returns nested list of indices and
    directions that word can be found
    >>> position_direction_word(['A', 'B', 'C', 'D', 'C', 'M'], 'AB')
    [[0,1]]
    >>> position_direction_word(['A', 'B', 'C', 'D', 'C', 'M'], 'CDC')
    [[2, 1], [4, -1]]
    >>> position_direction_word(['A', 'B', 'C', 'D', 'C', 'M'], 'CM')
    [[4, 1]]
    '''
    
    positions_and_directions = []
    
    first_letter = letter_positions(letter_list, word[0])
    #Finding all indices where first letter is
    
    for index in first_letter:
        directions = direction_word_given_position(letter_list, word, index)
        #List of directions that word is found for each index in previous list
        
        if len(directions) > 0:
            for direction in directions:
                sublist = [index, direction]
                #Creating nested lists of index and direction
                
                positions_and_directions.append(sublist)
    
    return positions_and_directions


def cross_word_position_direction(bool_letter_list, length_word,
                                  index, direction):
    '''
    (list, int, int, int) -> None
    Replaces value in bool_letter_list with True starting at
    index and for length of legth_word in direction given
    >>> bool_letter_list = [False, False, False, False, False, False]
    >>> cross_word_position_direction(bool_letter_list, 3, 0, 1)
    >>> bool_letter_list
    [True, True, True, False, False, False]
    >>> bool_letter_list = [False, False, False, False, False, False]
    >>> cross_word_position_direction(bool_letter_list, 2, 2, -1)
    >>> bool_letter_list
    [False, True, True, False, False, False]
    >>> bool_letter_list = [False, False, False, False, False, False]
    >>> cross_word_position_direction(bool_letter_list, 1, 3, 1)
    >>> bool_letter_list
    [False, False, False, True, False, False]
    '''
    i = 0
    while abs(i) < length_word:
        position = i + index
        #Changing boolean value
        bool_letter_list[position] = True
        i += direction


def cross_word_all_position_direction(bool_letter_list, length_word,
                                      list_position_direction):
    '''
    (list, int, list) -> None
    >>> bool_letter_list = [False, False, False, False, False,
    False, False]
    >>> cross_word_all_position_direction(bool_letter_list, 2, [[3, -1],
    [3, 1]])
    >>> bool_letter_list
    [False, False, True, True, True, False, False]
    >>> bool_letter_list = [False, False, False, False, False, False, False]
    >>> cross_word_all_position_direction(bool_letter_list, 3, [[0, 1],
    [6, -1]])
    >>> bool_letter_list
    [True, True, True, False, True, True, True]
    >>> bool_letter_list = [False, False, False, False, False, False, False]
    >>> cross_word_all_position_direction(bool_letter_list, 2, [[1, 1]])
    >>> bool_letter_list
    [False, True, True, False, False, False, False]
    
    '''
    for element in list_position_direction:
        #assigning index and direction (input parameters) from nested list
        index = element[0]
        direction = element[1]
        
        cross_word_position_direction(bool_letter_list, length_word,
                                      index, direction)
           

def find_magic_word(letter_list, bool_letter_list):
    '''
    (list, list) -> str
    Removes crossed out letters to reveal magic word. Raises error if input
    lists don't have the same size
    >>> find_magic_word(['C','A','B','C', 'D','O','M','P'], [False, True,
    True, True, True, False, False, False])
    COMP
    >>> find_magic_word(['A','B','C','D'], [True, True, True, True])
    
    >>> find_magic_word(['A','B','C','D'], [True, True, True])
    Traceback (most recent call last):
    ValueError: Both lists should have the same size
    '''
    
    #Raises error if lists don't have the same length
    if len(letter_list) != len(bool_letter_list):
        raise ValueError('Both lists should have the same size')
    
    magic_word = []
    
    for i in range(len(bool_letter_list)):
        if bool_letter_list[i] == False:
        
            letter = letter_list[i]
        
            magic_word.append(letter)
            #Adds all letters with value of True to list
    
    word = ''.join(magic_word) #converts list to string
    
    return word


def word_search(letter_list, word_list):
    '''
    (list, list) -> str
    Takes a list of letters and a list of strings and calls previous
    functions to find and return magic word
    >>> word_search(['C','W','I','K','I','P','E','D','I','A','O','M','M','O',
    'D','N','A','R','P'], ['WIKIPEDIA','RANDOM'])
    COMP
    >>> word_search(['C','W','I','K','I','P','E','D','I','A','O','M','M','O',
    'D','N','A','R','P'], ['WIKIPEDIA'])
    COMMODNARP
    >>> word_search(['C','W','I','K','I','P','E','D','I','A','O','M','M','O',
    'D','N','A','R','P'], ['RANDOM'])
    CWIKIPEDIAOMP
    '''
    bool_list = []
    #Creates boolean list with same length as letter_list 
    for i in range(len(letter_list)):
            bool_list.append(False)
            
    for word in word_list:
        length = len(word)
        
        index_list = position_direction_word(letter_list, word)
        #Gets nested list of directions and indexes using
        #position_direction_word
        
        cross_word_all_position_direction(bool_list, length, index_list)
        #updates bool_list for each word in word_list
        
    magic_word = find_magic_word(letter_list, bool_list)
    
    return magic_word


def word_search_main(letters, words):
    '''
    (str, str) -> str
    Converts letters to a list of characters and words to a list of words,
    and uses these to find the magic word
    >>> word_search_main('cwikipediaommodnarp', 'wikipedia-random')
    COMP
    >>> word_search_main('acompnjraviali', 'comp-ravi')
    ANJALI
    >>> word_search_main('haPPleellO', 'apple')
    HELLO
    '''
    letters = letters.upper() #converts string to uppercase
    letter_list = list(letters) #converts string to list
    
    words = words.upper()
    word_list = words.split('-') #converts string to list of word
    
    magic_word = word_search(letter_list, word_list)
    
    return magic_word


