# Shortest Word ---

def shortest_word(s): 
    # your lovely code here!
    converted_string = list(s.split(" ")) # split string into array of words
    shortest_word = converted_string[0] # shortest word is assigned to the first index in convertedstring array

    for i in converted_string: # loop through every word in convertedstring array
        if len(i) < len(shortest_word): # if the length of current word is less than the first word, assign it to new shortest word
            shortest_word = i
        return len(shortest_word)

print(shortest_word("I don't think that word means what you think it means"))
# should return: 1
  

# Sum of Minimums ---

def sum_of_minimums(list):
    # your lovely code goes here!
    return 'hello world'

my_list = [
    [1,2,3,4,5], # minimum value of row is 1
    [5,6,7,8,9], # minimum value of row is 5
    [20,21,34,56,100] # minimum value of row is 20
    ]

print(sum_of_minimums(my_list))
    # should return 26
  
# Split Strings

def split_strings(s):
    # your lovely code goes here
    return 'hello world'

print(split_strings('abc'))
# should return ['ab', 'c_']

print(split_strings('abcdef'))
# should return ['ab', 'cd', 'ef']
    
