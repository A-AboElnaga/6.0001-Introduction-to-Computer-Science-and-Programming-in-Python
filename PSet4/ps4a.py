# Problem Set 4A
# Name: A. Mongy
# Collaborators:
# Time Spent: 
   
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string
    
    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    word_original = sequence
    word = word_original
    # word = word_original.replace(" ","")              #removes spaces from the word
    # word = word.lower()                               #converts all letters to lowercase     
    word_list = list(word)
    
    if len(sequence) == 1:
        return [sequence]
    else:
        smaller_list = word_list.copy()
        perms=[]
        x= smaller_list[0]
        if len(smaller_list) >1:
            smaller_list.pop(0)   
        smaller_word= "".join(smaller_list)
        fewer_letter_list = get_permutations(smaller_word)
        
        for element in fewer_letter_list:
            listed_letters = list(element)
            counter = 0 
            while counter <= len(listed_letters):
                cpd_lstd_ltr = listed_letters.copy()
                cpd_lstd_ltr.insert(counter,x)
                counter = counter + 1
                new_word= "".join(cpd_lstd_ltr)
                perms.append(new_word)
    final_list= list(dict.fromkeys(perms)) #remove duplicates
    return final_list


if __name__ == '__main__':
#    #EXAMPLE
    example_input= input("Enter a word or numbers to get all possible permutations:" )
    print('Input:', example_input)
    if "a" in example_input and "b" in example_input and "c" in example_input:
        print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        print('Actual Output:', get_permutations(example_input))
        print('Number of all possible permutations',len(get_permutations(example_input)) )
    else:
          print('All possible permutations:', get_permutations(example_input))
          print('Number of all possible permutations',len(get_permutations(example_input)) )
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

