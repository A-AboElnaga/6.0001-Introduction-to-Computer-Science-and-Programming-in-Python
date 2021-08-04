# Problem Set 4B
#Name: A. Mongy
# Collaborators:
# Time Spent: x:xx

import string

LOWER_LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                 'n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPER_LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
### HELPER CODE ###

 

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
    def load_vaild_words(self):
        '''
        loads valid words

        Returns
        -------
        None.

        '''
        self.valid_words= load_words(WORDLIST_FILENAME)
        
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text 
        
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
    
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shifted_dict={}
        shift_int= shift
        for scanner in range(26):
            while shift_int >= 26 or scanner+shift_int >=26:
                shift_int= shift_int-26
            shifted_dict[LOWER_LETTERS[scanner]]=LOWER_LETTERS[scanner+shift_int]
            shifted_dict[UPPER_LETTERS[scanner]]=UPPER_LETTERS[scanner+shift_int]
        return(shifted_dict)
            

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_dict= self.build_shift_dict(shift)
        text= self.message_text
        encrypted_text=""
        for letter in text:
            if letter in UPPER_LETTERS or letter in LOWER_LETTERS:
                encrypted_text= encrypted_text +shifted_dict[letter]
            else:
                encrypted_text= encrypted_text + letter
                
        return(encrypted_text)
                
        
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self,text)
        self.shift = shift
        self.encryption_dict=self.build_shift_dict(shift)
        self.message_text_encrypted= self.apply_shift(shift)
        

        
            
        
        
       
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return(self.shift)
        
    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return(self.encryption_dict)
        
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return(self.message_text_encrypted)

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        PlaintextMessage.shift=self.shift
        
        return()

word_list= load_words(WORDLIST_FILENAME)
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text= text
        self.valid_words= self.get_valid_words
       
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        valid_shifts = {}
        all_possible_shifts=[]
        coded = ciphertext.message_text
        sep_words = []
        sep_words.extend(coded.split(' '))
        for scanner in range(26): 
            Vld_words_counter0= 0
            for word in sep_words:
               plaintext = PlaintextMessage(word, scanner)
               decoded = plaintext.get_message_text_encrypted()
               if is_word(word_list,decoded) == True:
                   Vld_words_counter0= Vld_words_counter0 + 1
                   all_possible_shifts.append(scanner)
                   print("the decoded word:", decoded,", its shifter:",scanner,'\n') 
                   
            valid_shifts[scanner]= Vld_words_counter0

        print("All shifts and how many words got decoded:",valid_shifts,'\n')
        max_key = max(valid_shifts, key=valid_shifts.get)
        plaintext =  PlaintextMessage(coded,max_key)
        success_word= plaintext.get_message_text_encrypted()
        all_possible_shifts_no_repeats = list(dict.fromkeys(all_possible_shifts))
        print("Possible shift(s) is/are : ", all_possible_shifts_no_repeats, '\n')        
        return( max_key,success_word)
        


story_string = get_story_string()

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    print('\ntesting encryption')
    plaintext = PlaintextMessage("hello", 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print('\n')


    #Example test case (CiphertextMessage)
    print("testing decrypt")
    ciphertext = CiphertextMessage("jgnnq")
    print('Expected Output', "hello")
    print('Actual Output:', ciphertext.decrypt_message())
    print('\n')

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    ciphertext = CiphertextMessage(story_string)
    print('Expected Output', ("decoded story"))
    print('Best Output: with shifter', ciphertext.decrypt_message())